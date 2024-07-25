import cv2
import mediapipe as mp
import pyautogui
import time

# Initialize Mediapipe Hands and Drawing modules
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Initialize OpenCV Video Capture
cap = cv2.VideoCapture(0)  # 0 means default camera

# Get screen size
screen_width, screen_height = pyautogui.size()

# Variables for double click detection
last_click_time = 0

def is_pinch_gesture(finger1, finger2, threshold=0.05):
    distance = ((finger1.x - finger2.x) ** 2 + (finger1.y - finger2.y) ** 2) ** 0.5
    return distance < threshold

def is_double_click():
    global last_click_time
    current_time = time.time()
    if current_time - last_click_time < 0.5:  # Double click interval
        return True
    last_click_time = current_time
    return False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the RGB image to detect hands
    result = hands.process(rgb_frame)

    # If hands are detected
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Draw hand landmarks on the frame
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get landmark positions
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            h, w, _ = frame.shape
            cursor_x, cursor_y = int(index_finger_tip.x * w), int(index_finger_tip.y * h)

            # Scale cursor position to screen size
            screen_x = int(cursor_x * screen_width / w)
            screen_y = int(cursor_y * screen_height / h)

            # Move cursor
            pyautogui.moveTo(screen_x, screen_y)

            # Left click (index finger and thumb touch)
            if is_pinch_gesture(thumb_tip, index_finger_tip):
                pyautogui.click()

            # Right click (index finger and middle finger touch)
            if is_pinch_gesture(index_finger_tip, middle_finger_tip):
                pyautogui.rightClick()

            # Double click (middle finger and thumb touch)
            if is_pinch_gesture(middle_finger_tip, thumb_tip) and is_double_click():
                pyautogui.doubleClick()

    # Display the resulting frame
    cv2.imshow('Handy cursor controller', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and destroy all windows
cap.release()
cv2.destroyAllWindows()
