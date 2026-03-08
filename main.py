import cv2
import mediapipe as mp
import pyautogui
import math
import numpy as np
import time

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
wCam, hCam = 640, 480
cap.set(3, wCam)
cap.set(4, hCam)

frameR = 120
smoothening = 5
deadzone = 2
click_threshold_time = 0.35

click_ratio_threshold = 0.18 


wScr, hScr = pyautogui.size()

plocX, plocY = 0, 0
clocX, clocY = 0, 0
drag_active = False        
pinch_start_time = 0       
pinch_flag = False         

with mp_hands.Hands(
    max_num_hands=1,
    model_complexity=1,
    min_detection_confidence=0.75,
    min_tracking_confidence=0.75) as hands:

    while True:
        success, img = cap.read()
        if not success:
            break
            
        img = cv2.flip(img, 1)

        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)
        
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                lmList = []
                for id, lm in enumerate(hand_landmarks.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id, cx, cy])

                if len(lmList) != 0:
                    x1, y1 = lmList[8][1], lmList[8][2]
                    x2, y2 = lmList[4][1], lmList[4][2]
                    x_wrist, y_wrist = lmList[0][1], lmList[0][2] 
                    x_index_base, y_index_base = lmList[5][1], lmList[5][2]

                    x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
                    y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
                    
                    x3 = np.clip(x3, 0, wScr)
                    y3 = np.clip(y3, 0, hScr)

                    clocX = plocX + (x3 - plocX) / smoothening
                    clocY = plocY + (y3 - plocY) / smoothening

                    if abs(clocX - plocX) > deadzone or abs(clocY - plocY) > deadzone:
                        pyautogui.moveTo(clocX, clocY)
                        plocX, plocY = clocX, clocY

                    cv2.circle(img, (x1, y1), 8, (0, 0, 255), cv2.FILLED) 

                    pinch_length = math.hypot(x2 - x1, y2 - y1)
                    hand_size_ref = math.hypot(x_index_base - x_wrist, y_index_base - y_wrist)
                    
                    if hand_size_ref == 0: 
                        hand_size_ref = 1
                        
                    pinch_ratio = pinch_length / hand_size_ref

                    cv2.putText(img, f'Ratio: {pinch_ratio:.2f}', (20, 450), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

                    if pinch_ratio < click_ratio_threshold:
                        cv2.circle(img, (x1, y1), 8, (0, 255, 0), cv2.FILLED) 
                        
                        if not pinch_flag:
                            pinch_flag = True
                            pinch_start_time = time.time()
                        
                        if (time.time() - pinch_start_time) > click_threshold_time:
                            if not drag_active:
                                pyautogui.mouseDown()
                                drag_active = True
                                cv2.putText(img, 'DRAGGING', (20, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 165, 255), 2)
                                
                    else:
                        if pinch_flag: 
                            pinch_duration = time.time() - pinch_start_time
                            
                            if pinch_duration < click_threshold_time:
                                pyautogui.click()
                                cv2.putText(img, 'CLICKED', (20, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
                            else:
                                if drag_active:
                                    pyautogui.mouseUp()
                                    drag_active = False

                            pinch_flag = False 
                            
                    if drag_active:
                         cv2.putText(img, 'DRAGGING', (20, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 165, 255), 2)

        cv2.imshow("Precision Virtual Mouse", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()