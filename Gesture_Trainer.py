import cv2
import mediapipe as mp
import numpy as np
import pickle  # To save the dataset

# Initialize MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Open webcam
cap = cv2.VideoCapture(0)

# Dictionary to store gesture data
gesture_data = {
    "thumbs_up": [],
    "fist": [],
    "open_palm": []
}

# Function to extract keypoints as a list
def get_hand_landmarks(landmarks):
    return [point.x for point in landmarks] + [point.y for point in landmarks]

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Convert landmarks to a feature vector
            keypoints = get_hand_landmarks(hand_landmarks.landmark)

            # Press a key to save gesture data
            key = cv2.waitKey(1) & 0xFF
            if key == ord("t"):  # Thumbs up
                gesture_data["thumbs_up"].append(keypoints)
                print("Saved Thumbs Up Gesture")
            elif key == ord("f"):  # Fist
                gesture_data["fist"].append(keypoints)
                print("Saved Fist Gesture")
            elif key == ord("o"):  # Open Palm
                gesture_data["open_palm"].append(keypoints)
                print("Saved Open Palm Gesture")

    cv2.imshow("Gesture Data Collection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

# Save dataset
with open("gesture_data.pkl", "wb") as f:
    pickle.dump(gesture_data, f)
