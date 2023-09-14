import time
import cv2  
import handtrackingmodule as htm

pTime = 0
cTime = 0 
cap = cv2.VideoCapture(0)
detector = htm.handDetect()
while True:
    success,img = cap.read()
    img = detector.findHands(img)
    PositionList = detector.findPos(img)
    ##number 4 in the position list detects the thumb
    if len(PositionList) != 0:
        print(PositionList[4])
 
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    
    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255),3)
    
    cv2.imshow('image',img)
    if cv2.waitKey(1) == ord('q'):
       break
