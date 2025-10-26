import cv2
import os
import random
import mediapipe as mp 
import hands_function
import pyautogui
from pynput.mouse import Button, Controller
mouse = Controller()



screen_width , screen_height = pyautogui.size()
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
    max_num_hands=1
)
  

def find_finger_tip(processed):
    if processed.multi_hand_landmarks:
        hand_landmarks = processed.multi_hand_landmarks[0]
       # print( hand_landmarks)
        return hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP]  
    
    return None

def move_mouse(index_finger_tip):
    if index_finger_tip is not None:
        scale_factor = 1
        x = int(index_finger_tip.x * screen_width * scale_factor)
        y = int(index_finger_tip.y * screen_height * scale_factor)


        x = min(max(0, x), screen_width - 1)
        y = min(max(0, y), screen_height - 1)
        pyautogui.moveTo(x, y)




def is_left_click(landmarks_list, thumb_index_dist):
    return (
        hands_function.get_angle(landmarks_list[5], landmarks_list[6], landmarks_list[8]) < 50 and
        hands_function.get_angle(landmarks_list[9], landmarks_list[10], landmarks_list[12]) > 90 and
        thumb_index_dist > 50
    )

def is_right_click(landmark_list, thumb_index_dist):
    return (
        hands_function.get_angle(landmark_list[9], landmark_list[10], landmark_list[12]) < 50 and
        hands_function.get_angle(landmark_list[5], landmark_list[6], landmark_list[8]) > 90 and
        thumb_index_dist > 50
    )

def is_double_click(landmark_list, thumb_index_dist):
    return (
        hands_function.get_angle(landmark_list[5], landmark_list[6], landmark_list[8]) < 50 and
        hands_function.get_angle(landmark_list[9], landmark_list[10], landmark_list[12]) < 50 and
        thumb_index_dist > 50
    )

def screenshot(landmark_list, thumb_index_dist):
    return (
        hands_function.get_angle(landmark_list[5], landmark_list[6], landmark_list[8]) < 50 and
        hands_function.get_angle(landmark_list[9], landmark_list[10], landmark_list[12]) < 50 and
        thumb_index_dist < 50
    )


        


save_folder = "screenshot_files"
os.makedirs(save_folder, exist_ok=True)  


def  detect_gestures(frame,landmarks_list,processed) :
    screenshot_taken = False

    if len(landmarks_list) >= 21 :
        index_finger_tip = find_finger_tip(processed)
        thumb_index_dist = hands_function.get_distance([landmarks_list[4], landmarks_list[5]])  

        if thumb_index_dist < 50 and  hands_function.get_angle(landmarks_list[5],landmarks_list[6],landmarks_list[8]) > 90 :

            move_mouse(index_finger_tip) 

        #left_click
        elif is_left_click(landmarks_list,thumb_index_dist):    
            mouse.press(Button.left)
            mouse.release(Button.left)
            cv2.putText(frame, "left_click",(50,50),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)

        
        #right_click
        elif is_right_click(landmarks_list,thumb_index_dist):   
           mouse.press(Button.right)
           mouse.release(Button.right)
           cv2.putText(frame, "right_click",(50,50),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)




        #double_click
        elif is_double_click(landmarks_list,thumb_index_dist): 
            pyautogui.doubleClick()
            cv2.putText(frame, "double_click",(50,50),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255),2)


        
        #screenshot
        elif screenshot(landmarks_list, thumb_index_dist):  
            if not screenshot_taken:
                counter = len([f for f in os.listdir(save_folder) if f.endswith('.png')]) + 1
        
                im1 = pyautogui.screenshot()
                file_path = os.path.join(save_folder, f'my_screenshot_{counter:03d}.png')
                im1.save(file_path)

                counter += 1  # Increment counter for next screenshot
                screenshot_taken = True
                cv2.putText(frame, "screenshot", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 2)
            else:
                 screenshot_taken = False
                
                    


    

def main():
    cap = cv2.VideoCapture(0)
    draw = mp.solutions.drawing_utils

    try:
        while cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                break

            frame = cv2.flip(frame, 1)
            frameRGB =cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            processed = hands.process(frameRGB)

            landmarks_list =[]

            if  processed.multi_hand_landmarks:
                hand_landmarks = processed.multi_hand_landmarks[0]
                draw.draw_landmarks(frame, hand_landmarks,mpHands.HAND_CONNECTIONS)

                for lm in hand_landmarks.landmark:
                      landmarks_list.append((lm.x,lm.y))

            detect_gestures(frame,landmarks_list,processed)          

                  

               



            cv2.imshow('mouse_control', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
