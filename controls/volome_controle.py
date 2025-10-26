import cv2
import numpy as np
import mediapipe as mp
from math import hypot
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

def main():
    # Configuration du volume
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    vol_range = volume.GetVolumeRange()
    min_vol, max_vol, _ = vol_range

    # Configuration MediaPipe
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        static_image_mode=False,
        model_complexity=1,
        min_detection_confidence=0.75,
        min_tracking_confidence=0.75,
        max_num_hands=1)

    draw = mp.solutions.drawing_utils
    cap = cv2.VideoCapture(0)
    
    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            processed = hands.process(frame_rgb)

            landmark_list = get_landmarks(frame, processed, draw, mp_hands)
            
            if landmark_list:
                distance = get_distance(frame, landmark_list)
                vol_level = np.interp(distance, [50, 150], [min_vol, max_vol])
                volume.SetMasterVolumeLevel(vol_level, None)

            cv2.imshow('Volume Control', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

def get_landmarks(frame, processed, draw, mp_hands):
    landmark_list = []
    
    if processed.multi_hand_landmarks:
        for hand_lm in processed.multi_hand_landmarks:
            for idx, landmark in enumerate(hand_lm.landmark):
                h, w, _ = frame.shape
                x, y = int(landmark.x * w), int(landmark.y * h)
                if idx == 4 or idx == 8:  # Pouce et index
                    landmark_list.append([idx, x, y])

            draw.draw_landmarks(frame, hand_lm, mp_hands.HAND_CONNECTIONS)
    
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