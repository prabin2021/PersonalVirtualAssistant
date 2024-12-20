import subprocess as sp
import cv2

def open_camera():
        sp.run('start microsoft.windows.camera:', shell=True)
        return "Camera opened sir"
def capture_photo():
        from main import speak
        camera = cv2.VideoCapture(0)
        return_value, image = camera.read()
        cv2.imwrite('D:/New_Virtual_Assistant/Face_Verification/captured_photo.jpg', image)
        del(camera)
        speak("Photo captured successfully!")
        return "Your photo has been captured sucessfully"