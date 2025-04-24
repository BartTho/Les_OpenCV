import cv2
from picamera2 import Picamera2

# Video inlezen
#cap = cv2.VideoCapture(1)

PiCam = Picamera2()

# Run hand voor camera blauw
PiCam.preview_configuration.main.format='RGB888'

PiCam.preview_configuration.main.size=(1920, 1080)
#PiCam.preview_configuration.main.size=(800, 600)
PiCam.preview_configuration.align()

PiCam.configure("preview")
PiCam.start()

while True:
    frame = PiCam.capture_array()
    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

PiCam.stop_preview()
cv2.destroyAllWindows()