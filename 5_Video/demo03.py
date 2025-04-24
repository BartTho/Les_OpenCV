import cv2
from picamera2 import Picamera2
import time

dispB=1280
dispH=720

def onTrack1(val):
    global xPos
    xPos=val
    print('xPos',xPos)
def onTrack2(val):
    global yPos
    yPos=val
    print('yPos',yPos)
def onTrack3(val):
    global Breedte
    Breedte=val
    print('Breedte',Breedte)
def onTrack4(val):
    global Hoogte
    Hoogte=val
    print('Hoogte',Hoogte)

picam2 = Picamera2()

picam2.preview_configuration.main.size = (dispB,dispH)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.controls.FrameRate=30
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()
fps=0
pos=(30,60)
font=cv2.FONT_HERSHEY_SIMPLEX
height=1.5
weight=3
myColor=(0,0,255)

cv2.namedWindow('mijnTracker')
 
cv2.createTrackbar('X Pos','mijnTracker',10,dispB,onTrack1)
cv2.createTrackbar('Y Pos','mijnTracker',10,dispH,onTrack2)
cv2.createTrackbar('Box Breedte','mijnTracker',100,255,onTrack3)
cv2.createTrackbar('Box Hoogte','mijnTracker',255,255,onTrack4)

while True:
    tStart=time.time()
    frame= picam2.capture_array()
    cv2.putText(frame,str(int(fps))+' FPS',pos,font,height,myColor,weight)
    cv2.rectangle(frame,(xPos,yPos),(xPos+Breedte,yPos+Hoogte),(0,255,0),2)
    ROI=frame[yPos:yPos+Hoogte,xPos:xPos+Breedte]    
    cv2.imshow("Camera", frame)
    cv2.imshow("ROI",ROI)
    if cv2.waitKey(1)==ord('q'):
        break
    tEnd=time.time()
    loopTime=tEnd-tStart
    fps=.9*fps + .1*(1/loopTime)
cv2.destroyAllWindows()