def take_sample():
    import pickle
    import cv2
    import face_recognition
    import os
    count = 0
    sample_to_take = 200 

    user_name = input("Please enter your name: ")

    # Create a directory to store face samples, if it doesn't exist
    if not os.path.exists(f"D:/New_Virtual_Assistant/Face_Verification/face_samples/{user_name}"):
        os.makedirs(f"D:/New_Virtual_Assistant/Face_Verification/face_samples/{user_name}")

    # Capture face samples from the camera
    video_capture = cv2.VideoCapture(0)
    print(f"Please wait! I am collecting the {sample_to_take} face samples of {user_name}\n")

    while count < sample_to_take:
        status, frame = video_capture.read()
        facelocations = face_recognition.face_locations(frame)
        if facelocations:
            count += 1
            cv2.imwrite(f"D:/New_Virtual_Assistant/Face_Verification/face_samples/{user_name}/{user_name}_sample_{count}.jpg", frame)
            print(f"Sucessfully collected {count}/{sample_to_take} face samples.")
        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cv2.destroyAllWindows()
    video_capture.release()

    sample_folder_name = f"D:/New_Virtual_Assistant/Face_Verification/face_samples/{user_name}"
    if not os.path.exists(sample_folder_name):
        print(f"No face samples found for {user_name} in {sample_folder_name}.")
        exit()

    encodings = []
    print(f"Please wait! I am generating encodings for {user_name}'s face samples.\n")

    for img_file in os.listdir(sample_folder_name):
        image_path = os.path.join(sample_folder_name, img_file)
    

        img = cv2.imread(image_path)
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        facelocations = face_recognition.face_locations(rgb_img)
        face_encodings = face_recognition.face_encodings(rgb_img, facelocations)

        if face_encodings:
            encodings.append(face_encodings[0])

    if not encodings:
        print(f"No face can be detected in the images for {user_name}.")
        exit()

    encodings_file = f"D:/New_Virtual_Assistant/Face_Verification/{user_name}_encodings.pkl"
    with open(encodings_file, "wb") as f:
        pickle.dump({"encodings": encodings, "name": user_name}, f)

    print(f"Encodings for {user_name} saved to {encodings_file}.")

# take_sample()