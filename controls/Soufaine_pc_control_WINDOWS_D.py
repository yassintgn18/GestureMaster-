import cv2
import mediapipe as mp
import pyautogui

pyautogui.FAILSAFE = False


mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

sensitivity = 1 


prev_y = None
swipe_threshold = 100

while cap.isOpened():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)  
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

         
            y = int(hand_landmarks.landmark[8].y * frame.shape[0])

            
            if prev_y is not None:
                if y > prev_y + swipe_threshold:  
                    pyautogui.hotkey('win', 'd')  
                    print("Swiped down! Minimized all windows.")  

            
            prev_y = y

    cv2.imshow("Hand Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
