def take_sample():
    import pickle
    import cv2
    import face_recognition
    import os
    sample_limit = 100  # Number of samples to capture
    sample_count = 0

    # Ask the user for their name
    user_name = input("Please enter your name: ")

    # Create a directory to store face samples, if it doesn't exist
    if not os.path.exists(f"face_samples/{user_name}"):
        os.makedirs(f"face_samples/{user_name}")

    # Capture face samples from the camera
    video_capture = cv2.VideoCapture(0)
    print(f"Collecting {sample_limit} face samples of {user_name}\n")

    while sample_count < sample_limit:
        ret, frame = video_capture.read()
        facelocations = face_recognition.face_locations(frame)

        if facelocations:
            # Only save the image if a face is detected
            sample_count += 1
            # Save the image with a unique name
            cv2.imwrite(f"face_samples/{user_name}/{user_name}_sample_{sample_count}.jpg", frame)
            print(f"Collected {sample_count}/{sample_limit} face samples.")
        
        # Display the current frame while collecting samples
        cv2.imshow(f"Collecting Face Samples for {user_name}", frame)
        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Path to the folder where face samples are stored
    cv2.destroyAllWindows()
    video_capture.release()


    sample_folder = f"face_samples/{user_name}"
    # Check if the folder exists
    if not os.path.exists(sample_folder):
        print(f"No face samples found for {user_name} in {sample_folder}.")
        exit()

    encodings = []
    print(f"Generating encodings of {user_name}'s face samples.\n")
    # Iterate over all the sample images for this user
    for img_file in os.listdir(sample_folder):
        img_path = os.path.join(sample_folder, img_file)
        
        # Load the image
        img = cv2.imread(img_path)
        
        # Convert the image from BGR (OpenCV's format) to RGB (required by face_recognition)
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Detect face locations
        facelocations = face_recognition.face_locations(rgb_img)
        
        # Get the face encodings for the detected face(s)
        face_encodings = face_recognition.face_encodings(rgb_img, facelocations)
        
        # We only expect one face per image, so take the first encoding
        if face_encodings:
            encodings.append(face_encodings[0])  # Store the first face encoding

    # If no encodings are found, exit
    if not encodings:
        print(f"No faces detected in the images for {user_name}.")
        exit()

    # Save the encodings to a .pkl file
    encodings_file = f"{user_name}_encodings.pkl"
    with open(encodings_file, "wb") as f:
        pickle.dump({"encodings": encodings, "name": user_name}, f)

    print(f"Encodings for {user_name} saved to {encodings_file}.")

