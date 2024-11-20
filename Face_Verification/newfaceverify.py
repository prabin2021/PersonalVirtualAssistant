import cv2
import face_recognition
import pickle
import os

# Load the saved encodings from the .pkl file
def load_encodings(encodings_dir):
    all_encodings = []
    all_names = []
    
    # Iterate through each encoding file in the directory
    for file_name in os.listdir(encodings_dir):
        if file_name.endswith("_encodings.pkl"):
            with open(os.path.join(encodings_dir, file_name), "rb") as f:
                data = pickle.load(f)
                all_encodings.extend(data["encodings"])
                all_names.extend([data["name"]] * len(data["encodings"]))  # Repeat the name for each encoding
    
    return all_encodings, all_names
def verifyface():
    encodings_dir = "D:/Jarwis_Pro/Latest_Project/New_Virtual_Assistant/Face_Verification/face_encoding"
    # Initialize video capture
    video_capture = cv2.VideoCapture(0)
    # Load encodings and names
    encodings, names = load_encodings(encodings_dir)
    print("Loading face encodings...")
    print(f"Loaded {len(encodings)} encodings for {len(set(names))} users.")

    while True:
        ret, frame = video_capture.read()
        
        # Convert the image from BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Find all the face locations and encodings in the current frame
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Compare the current face encoding with known encodings
            matches = face_recognition.compare_faces(encodings, face_encoding,tolerance=0.5)
            name = "Unknown"  # Default name if no match found

            # If a match is found, use the first match
            if True in matches:
                first_match_index = matches.index(True)
                name = names[first_match_index]
                
                return matches
            # Draw a rectangle around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        # Display the resulting frame
        cv2.imshow("Face Recognition", frame)
        
        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    # # Release the video capture and close windows
    # video_capture.release()
    # cv2.destroyAllWindows()

