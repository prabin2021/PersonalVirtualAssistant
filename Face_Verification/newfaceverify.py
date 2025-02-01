import cv2
import face_recognition
import pickle
import os
import matplotlib.pyplot as plt

def load_all_encodings(encodings_dir):
    names = []
    encodings = []
    for file_name in os.listdir(encodings_dir):
        if file_name.endswith("_encodings.pkl"):
            with open(os.path.join(encodings_dir, file_name), "rb") as f:
                data = pickle.load(f)
                encodings.extend(data["encodings"])
                names.extend([data["name"]] * len(data["encodings"]))  
    return encodings, names

def compare_faces(known_face_encodings, face_encoding_to_check, tolerance=0.3):
    distances = face_distance(known_face_encodings, face_encoding_to_check)
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
    video_capture = cv2.VideoCapture(0)
    if not video_capture.isOpened():
        return "Error: Could not open camera."
    encodings, names = load_all_encodings(encodings_dir)
    true_count = 0
    false_count = 0
    false_threshold = 5
    while True:
        status, frame = video_capture.read()
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)    
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matched = compare_faces(encodings, face_encoding,tolerance=0.3)
            name = "Unknown" 
            if True in matched:
                name = "Verified"
                true_count += 1
            else:
                false_count += 1
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        if true_count > false_count and true_count >= 3:
                video_capture.release()
                cv2.destroyAllWindows()
                return True 
        if false_count > false_threshold:
                video_capture.release()
                cv2.destroyAllWindows()
                return False 
        cv2.imshow("Face Recognition", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

def plot_dotted_accuracy(results):
    if not results:
        return "No face verifications performed."
    attempts = list(range(1, len(results) + 1))  # X-axis: Attempt numbers
    y_values = [1 if result else 0 for result in results]  # 1 for success, 0 for failure

    # Calculate accuracy percentage
    success_count = sum(results)
    total_attempts = len(results)
    accuracy_percentage = (success_count / total_attempts) * 100

    plt.figure(figsize=(10, 6))
    plt.scatter(attempts, y_values, c=['green' if r else 'red' for r in results], marker='o', edgecolors='black')

    plt.xlabel("Verification Attempts")
    plt.ylabel("Verification Result (Green dot = Success, Red dot = Failure)")
    plt.title(f"Face Verification Accuracy: {accuracy_percentage:.2f}%")  # Show accuracy in title
    plt.yticks([0, 1], ["Failure", "Success"])
    plt.grid(axis='y', linestyle='dotted')

    # Display accuracy & attempts at the bottom of the plot
    plt.figtext(0.5, -0.1, f"Total Attempts: {total_attempts} | Accuracy: {accuracy_percentage:.2f}%", 
                ha="center", fontsize=12, bbox={"facecolor": "lightgray", "alpha": 0.5, "pad": 5})
    plt.show(block=True)  # Force Matplotlib to wait
    plt.close()
    return accuracy_percentage

def analyze_face():
    encodings_dir = "D:/New_Virtual_Assistant/Face_Verification"
    video_capture = cv2.VideoCapture(0)
    if not video_capture.isOpened():
        return "Error: Could not open camera."
    encodings, names = load_all_encodings(encodings_dir)
    results = []
    while True:
        status, frame = video_capture.read()
        if not status:
            continue  
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)    

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matched = compare_faces(encodings, face_encoding, tolerance=0.3)
            name = "Unknown"
            if True in matched:
                name = "Verified"
                results.append(True)
            else:
                results.append(False)   
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        cv2.imshow("Face Recognition", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    video_capture.release()
    cv2.destroyAllWindows()
    result= plot_dotted_accuracy(results)
    return result
