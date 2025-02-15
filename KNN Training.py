import pickle
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Load dataset
with open("gesture_data.pkl", "rb") as f:
    gesture_data = pickle.load(f)

# Prepare training data
X = []  # Feature vectors (hand keypoints)
y = []  # Labels

for gesture, data in gesture_data.items():
    X.extend(data)
    y.extend([gesture] * len(data))

X = np.array(X)
y = np.array(y)

# Train KNN model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)

# Save trained model
with open("gesture_classifier.pkl", "wb") as f:
    pickle.dump(knn, f)

print("Gesture Classifier Trained and Saved!")
