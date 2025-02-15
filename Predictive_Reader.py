import cv2
import mediapipe as mp
import pickle

# Load trained model
with open("gesture_classifier.pkl", "rb") as f:
    knn = pickle.load(f)

# Initialize MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Function to extract keypoints from hand landmarks
def get_hand_landmarks(landmarks):
    return [point.x for point in landmarks] + [point.y for point in landmarks]

# Function to detect thumbs up
def is_thumbs_up(landmarks):
    thumb_tip = landmarks[4]   # Thumb tip
    thumb_base = landmarks[2]  # Lower thumb joint
    index_tip = landmarks[8]   # Index finger tip
    pinky_tip = landmarks[20]  # Pinky tip

    if thumb_tip.y < index_tip.y and thumb_tip.y < pinky_tip.y:
        if abs(thumb_tip.x - thumb_base.x) > 0.1:
            return True
    return False

# Start webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Extract keypoints
            landmarks = hand_landmarks.landmark

            # Use classifier to predict gesture
            keypoints = get_hand_landmarks(landmarks)
            prediction = knn.predict([keypoints])[0]

            # Display gesture prediction
            cv2.putText(frame, f"Gesture: {prediction}", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

            # Also check for thumbs-up manually
            if is_thumbs_up(landmarks):
                print("👍 Thumbs Up Detected!")

    cv2.imshow("Hand Gesture Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
