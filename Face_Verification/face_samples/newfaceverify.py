import cv2
import face_recognition
import pickle
import os



# Load the saved encodings from the .pkl file
def load_all_encodings(encodings_dir):
    names = []
    encodings = []
    
    # Iterate through each encoding file in the directory
    for file_name in os.listdir(encodings_dir):
        if file_name.endswith("_encodings.pkl"):
            with open(os.path.join(encodings_dir, file_name), "rb") as f:
                data = pickle.load(f)
                encodings.extend(data["encodings"])
                names.extend([data["name"]] * len(data["encodings"]))  # Repeat the name for each encoding
  
    return encodings, names

def compare_faces(known_face_encodings, face_encoding_to_check, tolerance=0.3):
    distances = face_distance(known_face_encodings, face_encoding_to_check)
    # Return a list of boolean values where True means a match
    return [distance <= tolerance for distance in distances]

def face_distance(face_encodings, face_to_compare):
    if len(face_encodings) == 0:
        return []  
    distances = []  
    for encoding in face_encodings:
        squared_diff = [(a - b) ** 2 for a, b in zip(encoding, face_to_compare)]  
        distance = sum(squared_diff) ** 0.5  
        distances.append(distance)  
    return distances


def verifyface():
    encodings_dir = "D:/New_Virtual_Assistant/Face_Verification"
    # Initialize video capture
    video_capture = cv2.VideoCapture(0)
      # Use index 0 for the default camera
    if not video_capture.isOpened():
        return "Error: Could not open camera."
    # Load encodings and names
    encodings, names = load_all_encodings(encodings_dir)
    print("Loading face encodings...")
    print(f"Loaded {len(encodings)} encodings for {len(set(names))} users.")
    true_count = 0
    false_count = 0
    false_threshold = 5
    while True:
        status, frame = video_capture.read()
        # Convert the image from BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Find all the face locations and encodings in the current frame
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)    
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Compare the current face encoding with known encodings
            matched = compare_faces(encodings, face_encoding,tolerance=0.3)
            name = "Unknown"  # Default name if no match found
            # If a match is found, use the first match
            if True in matched:
                # Successful match
                first_match_index = matched.index(True)
                name = names[first_match_index]
                true_count += 1
                print(f"{name} face detected")
            else:
                # Unsuccessful match
                false_count += 1
                
            # Draw a rectangle around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

            # If sufficient true matches, allow access
        if true_count > false_count and true_count >= 3:
                print(f"Access Granted to {name}.")
                video_capture.release()
                cv2.destroyAllWindows()
                return True 
        if false_count > false_threshold:
                print("Too many false attempts! Access Denied.")
                video_capture.release()
                cv2.destroyAllWindows()
                return False  # Deny access due to too many false matches
        # Display the resulting frame
        cv2.imshow("Face Recognition", frame)
        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
# verifyface()