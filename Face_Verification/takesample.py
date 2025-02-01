def take_sample():
    
    import pickle
    import cv2
    import face_recognition
    import os
    count = 0
    sample_to_take =100
    if not os.path.exists(f"D:/New_Virtual_Assistant/Face_Verification/face_samples/Samples"):
        os.makedirs(f"D:/New_Virtual_Assistant/Face_Verification/face_samples/Samples")
    video_capture = cv2.VideoCapture(0)
    while count < sample_to_take:
        status, frame = video_capture.read()
        facelocations = face_recognition.face_locations(frame)
        if facelocations:
            count += 1
            cv2.imwrite(f"D:/New_Virtual_Assistant/Face_Verification/face_samples/Samples/_sample_{count}.jpg", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cv2.destroyAllWindows()
    video_capture.release()
    sample_folder_name = f"D:/New_Virtual_Assistant/Face_Verification/face_samples/Samples"
    if not os.path.exists(sample_folder_name):
        return "No face samples found"
    encodings = []
    for img_file in os.listdir(sample_folder_name):
        image_path = os.path.join(sample_folder_name, img_file)
        img = cv2.imread(image_path)
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
        facelocations = face_recognition.face_locations(rgb_img)
        face_encodings = face_recognition.face_encodings(rgb_img, facelocations)
        if face_encodings:
            encodings.append(face_encodings[0])
    if not encodings:
        return "No face can be detected in the images"
    encodings_file = f"D:/New_Virtual_Assistant/Face_Verification/Face_encodings.pkl"
    with open(encodings_file, "wb") as f:
        pickle.dump({"encodings": encodings, "name": "Samples"}, f)
    return "Encodings generated for provided face samples"
