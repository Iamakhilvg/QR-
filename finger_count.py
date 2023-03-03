import mediapipe as mp
import cv2
mp_hands=mp.solutions.hands
draw=mp.solutions.drawing_utils
hands=mp_hands.Hands(max_num_hands=1,min_detection_confidence=.7)

cap=cv2.VideoCapture(0)
while True:
    sucess,img=cap.read()
    img=cv2.flip(img,1)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(img)
    img=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    

    
    rec=cv2.rectangle(img,(20,350),(90,440),(255,0,0),cv2.FILLED)
    rec1 = cv2.circle(img, radius=30, center=(55, 390), color=(0, 255, 255), thickness=2)

    tipids=[4,8,12,16,20]
    lmlist=[]

    if results.multi_hand_landmarks:

        for handlms in results.multi_hand_landmarks:
            for id,lm in enumerate(handlms.landmark):
                cx=lm.x
                cy=lm.y
                lmlist.append([id,cx,cy])
                if len(lmlist)!=0 and len(lmlist)==21:
                    fingerlist=[]
                    if lmlist[12][1]>lmlist[20][1]:
                        if lmlist[tipids[0]][1]>lmlist[tipids[0]-1][1]:
                            fingerlist.append(1)
                        #else:
                            #fingerlist.append(0)
                    else:
                        if lmlist[tipids[0]][1]<lmlist[tipids[0]-1][1]:
                            fingerlist.append(1)
                        #else:
                            #fingerlist.append(0)
                    
                        

                    for i in range(1,5):#except thumb
                        if lmlist[tipids[i]][2]<lmlist[tipids[i]-2][2]:
                            fingerlist.append(1)
                        #else:
                            #fingerlist.append(0)
                     
                    # print(len(fingerlist))
                    n=(len(fingerlist))
            cv2.putText(rec,str(n),(45,405),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),0)
        draw.draw_landmarks(img,handlms,mp_hands.HAND_CONNECTIONS,draw.DrawingSpec(color=(0,255,0),thickness=2),draw.DrawingSpec(color=(0,0,0),thickness=2))



        

            
            

    


    cv2.imshow('finger',img)
    if cv2.waitKey(1) & 0XFF==ord('q'):
        break
cv2.destroyAllWindows()
print(lmlist)
        

