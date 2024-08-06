Hand Gesture-Based Cursor Control System
This project lets you control your computer's cursor using hand gestures. It uses Python with OpenCV, Mediapipe, and PyAutoGUI.

Features
Cursor Movement: Move the cursor using your index finger.
Left Click: Touch your index finger and thumb together to left click.
Right Click: Touch your index finger and middle finger together to right click.
Double Click: Touch your middle finger and thumb together to double click.

Modules Used
OpenCV: For capturing video from the webcam.
Mediapipe: For detecting hand landmarks.
PyAutoGUI: For controlling the mouse.

Use the following gestures:
Move the cursor: Use your index finger to move the cursor.
Left Click: Touch your index finger and thumb together.
Right Click: Touch your index finger and middle finger together.
Double Click: Touch your middle finger and thumb together.

How It Works
Capture Video: The script captures video from your webcam.
Detect Hand Landmarks: Mediapipe detects the landmarks of your hand.
Map Movements: The script maps your hand movements to cursor movements.
Recognize Gestures: Specific gestures trigger mouse actions (left click, right click, double click).
