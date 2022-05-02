import cv2
import mediapipe as mp
import time

#using webcam 1
cap=cv2.VideoCapture(0)

#for using model
mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils

#for checking frame rate
pTime=0
cTime=0

while True:
    #video capturing
    success, img=cap.read()
    #coverting image to RGB
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    #getting results after applying hand tracking module
    results=hands.process(imgRGB)

    # print(results.multi_hand_landmarks)

    #drawing landmarks on multiple hands
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:

            for id,lm in enumerate(handLms.landmark):
                #print(id,lm)
                h,w,c=img.shape
                #getting the coordinates
                cx,cy=int(lm.x*w),int(lm.y*h)
                print(id,cx,cy)
                

            #drawing landmarks on multiple hands
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
    
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    
    #printing fps on screen
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,255),3)
    
    #showing results
    cv2.imshow("Image",img)
    cv2.waitKey(1)