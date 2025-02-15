import cv2
import mediapipe as mp

# Initialize MediaPipe Hand model
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Open webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to RGB (MediaPipe requires RGB format)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    # Draw hand landmarks
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Extract keypoints
            landmarks = hand_landmarks.landmark

            if is_thumbs_up(landmarks):
                print("👍 Thumbs Up Detected!")

    cv2.imshow("Hand Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

def is_thumbs_up(landmarks):
    thumb_tip = landmarks[4]
    thumb_base = landmarks[2]
    index_tip = landmarks[8]
    pinky_tip = landmarks[20]

    # Check if thumb is above the index and pinky
    if thumb_tip.y < index_tip.y and thumb_tip.y < pinky_tip.y:
        # Check if thumb is extended outward
        if abs(thumb_tip.x - thumb_base.x) > 0.1:
            return True
    return False
