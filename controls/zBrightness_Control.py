import cv2
import numpy as np
import mediapipe as mp
import screen_brightness_control as sbc
from math import hypot

def main():
    mpHands = mp.solutions.hands
    hands = mpHands.Hands(
        static_image_mode=False,
        model_complexity=1,
        min_detection_confidence=0.75,
        min_tracking_confidence=0.75,
        max_num_hands=1)

    draw = mp.solutions.drawing_utils
    cap = cv2.VideoCapture(0)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 300)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 350)
    
    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            processed = hands.process(frameRGB)

            left_landmark_list = get_landmarks(frame, processed, draw, mpHands)
            
            if left_landmark_list:
                left_distance = get_distance(frame, left_landmark_list)
                b_level = np.interp(left_distance, [50, 150], [0, 180])
                sbc.set_brightness(int(b_level))

            cv2.imshow('Brightness Control', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

def get_landmarks(frame, processed, draw, mpHands):
    landmark_list = []
    
    if processed.multi_hand_landmarks:
        for handlm in processed.multi_hand_landmarks:
            for idx, found_landmark in enumerate(handlm.landmark):
                height, width, _ = frame.shape
                x, y = int(found_landmark.x * width), int(found_landmark.y * height)
                if idx == 4 or idx == 8:
                    landmark_list.append([idx, x, y])

            draw.draw_landmarks(frame, handlm, mpHands.HAND_CONNECTIONS)
    
    return landmark_list

def get_distance(frame, landmark_list):
    if len(landmark_list) < 2:
        return 0
    (x1, y1), (x2, y2) = (landmark_list[0][1], landmark_list[0][2]), \
                          (landmark_list[1][1], landmark_list[1][2])
    cv2.circle(frame, (x1, y1), 7, (0, 255, 0), cv2.FILLED)
    cv2.circle(frame, (x2, y2), 7, (0, 255, 0), cv2.FILLED)
    cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
    
    return hypot(x2 - x1, y2 - y1)

if __name__ == '__main__':
    main()
