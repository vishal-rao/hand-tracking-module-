import mediapipe as mp
import time
import cv2  

class handDetect():
   def __init__(self, mode=False, maxHands=2, modelComplexity=1, detectionCon=0.1, trackCon=0.7):
       self.mode = mode
       self.maxHands = maxHands
       self.detectionCon = detectionCon
       self.modelComplex = modelComplexity
       self.trackCon = trackCon
       self.mpHands = mp.solutions.hands
       self.hands = self.mpHands.Hands(self.mode, self.maxHands,self.modelComplex,self.detectionCon, self.trackCon)
       self.mpDraw = mp.solutions.drawing_utils

   def findHands(self,img,draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
            ##gives the result about detecting hands and their coordinates
            #print(results.multi_hand_landmarks)
        
        if self.results.multi_hand_landmarks:
                for handLms in self.results.multi_hand_landmarks:
                    if draw:
                        self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
        return img

   def findPos(self,img,handNo=0,draw = True):
        PositionList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            
            for id,lm in enumerate(myHand.landmark):
                #print(id,lm)
                h,w,c = img.shape
                cx,cy = int(lm.x*w),int(lm.y*h)
                #print(id,cx,cy)
                PositionList.append([id,cx,cy])
                
                ##Size of the circles on the landmarks  
                if draw:
                    cv2.circle(img,(cx,cy),10,(255,0,255),cv2.FILLED)
        return PositionList

            
  
   
def main():
   

 if __name__ == "__main__": 
    main()
    
