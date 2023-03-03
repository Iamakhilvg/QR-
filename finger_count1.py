import mediapipe
import cv2
medhands=mediapipe.solutions.hands
draw=mediapipe.solutions.drawing_utils
hands=medhands.Hands(max_num_hands=1,min_detection_confidence=0.7)

cap=cv2.VideoCapture(0)
while True:
    success,img=cap.read()
    img=cv2.flip(img,1)
    imgrgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    res=hands.process(imgrgb)
    
    cv2.rectangle(img,(20,350),(90,440),(0,255,0),cv2.FILLED)
    tipids=[4,8,12,16,20]
    lmlist=[]

    if res.multi_hand_landmarks:
        for handlms in res.multi_hand_landmarks:
            for id,lm in enumerate(handlms.landmark):
                cx=lm.x
                cy=lm.y
                lmlist.append([id,cx,cy])
                
                if len(lmlist)!=0 and len(lmlist)==21:

                    fingerlist=[]

                    for i in range(0,5):

                      if lmlist[tipids[i]][2]<lmlist[tipids[i]-2][2]:
                          fingerlist.append(1)
                      else:
                           fingerlist.append(0)
                    print(fingerlist)