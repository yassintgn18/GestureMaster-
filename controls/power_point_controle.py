import cv2
import mediapipe as mp
import pyautogui
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

cap = cv2.VideoCapture(0)
last_press_time = 0
press_cooldown = 0.5  # Cooldown réduit à 0.5s
GESTURE_ZONE_WIDTH = 100  # Zones de 100px

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        hand_landmarks = result.multi_hand_landmarks[0]
        landmarks = hand_landmarks.landmark
        
        index_x = int(landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * w)
        index_y = int(landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * h)

        # Zones ajustées
        cv2.rectangle(frame, (0, 0), (GESTURE_ZONE_WIDTH, h), (0, 255, 0), 2)
        cv2.rectangle(frame, (w-GESTURE_ZONE_WIDTH, 0), (w, h), (0, 255, 0), 2)

        current_time = time.time()
        if current_time - last_press_time > press_cooldown:
            if index_x < GESTURE_ZONE_WIDTH:
                pyautogui.press("left")
                last_press_time = current_time
                cv2.putText(frame, "PREVIOUS", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            elif index_x > w - GESTURE_ZONE_WIDTH:
                pyautogui.press("right")
                last_press_time = current_time
                cv2.putText(frame, "NEXT", (w-150, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("PowerPoint Control", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()