# **Open-Source Hand Gesture Recognition with KNN**
### **Train Your Own Hand Gesture Model for Custom Applications**  

🚀 **This project provides an easy-to-use pipeline for training a KNN-based hand gesture recognition model.**  
The goal is to allow users to **define, train, and recognize** their own hand gestures without requiring deep learning expertise.  
This will later be used for **prosthetic control**, where users can customize gestures for their prosthetic hands.

---

## **🔹 Features**
✅ **Train a custom hand gesture model** using your own hand movements  
✅ **Uses MediaPipe for real-time hand tracking**  
✅ **K-Nearest Neighbors (KNN) classifier for lightweight gesture recognition**  
✅ **Open-source and adaptable for different use cases**  
✅ **Easily expand gesture sets for various applications**  

---

## **📌 Future Applications**
This system is designed as **a foundation for a future prosthetic control system**.  
- Users can **train their own gestures**, allowing for **personalized prosthetic hand control**.  
- The trained model can be **exported to hardware** for **gesture-to-movement conversion**.  
- This project enables **rapid prototyping** for **robotics, assistive devices, and hands-free control systems**.  

---

## **🚀 Getting Started**
### **🔹 Installation**
Make sure you have **Python 3.8+** installed.  

1️⃣ **Clone this repository**:
```bash
git clone https://github.com/yourusername/Hand-Gesture-KNN.git
cd Hand-Gesture-KNN
```

2️⃣ **Set up a virtual environment (recommended)**:
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

3️⃣ **Install dependencies**:
```bash
pip install -r requirements.txt
```

---

## **🖐️ Training Your Own Gestures**
1️⃣ **Run the Gesture Data Collection Script**  
This will allow you to record your own hand gestures.  

```bash
python gesture_data_collection.py
```
🎥 **How it works:**  
- The webcam will open.  
- Perform your gesture and press a key to label it:
  - **`T`** → Save "Thumbs Up"  
  - **`F`** → Save "Fist"  
  - **`O`** → Save "Open Palm"  
- Press **`Q`** to exit.  
- The recorded gestures are saved in **`gesture_data.pkl`**.

---

2️⃣ **Train Your Gesture Model**  
After collecting data, train the KNN model with:
```bash
python gesture_trainer.py
```
🎯 **What happens here?**  
- Your recorded hand keypoints are loaded from `gesture_data.pkl`.  
- A **KNN classifier** is trained based on your labeled gestures.  
- The trained model is saved as **`gesture_classifier.pkl`**.

---

3️⃣ **Test the Trained Model (Live Gesture Prediction)**
Run:
```bash
python Webcam_Gesture.py
```
🎥 **This will open the webcam and start recognizing gestures in real time.**  
You’ll see predicted gestures displayed on the screen.

---

## **🛠️ How It Works**
### **🔹 Key Technologies**
- **MediaPipe Hands** → Real-time hand landmark detection
- **OpenCV** → Webcam processing & visualization
- **Scikit-Learn (KNN)** → Lightweight machine learning for classifying gestures

### **🔹 How Gestures Are Recognized**
1. The webcam **captures your hand position**.
2. MediaPipe extracts **21 key landmarks** (fingertips, joints, palm center).
3. A KNN classifier **matches the keypoints** to your trained gestures.
4. The predicted gesture is **displayed on the screen**.

---

## **🎯 Adapting This for Prosthetic Control**
This project is designed for **future prosthetic applications**.  
👋 **How will it work?**
1. **Users train their own gestures** to match desired prosthetic movements.
2. The system **translates gestures into control signals**.
3. The trained model is **integrated into a prosthetic hand’s software**, mapping gestures to physical movements.

📌 **Future Steps:**
- Convert gesture predictions into **serial data for prosthetic communication**.
- Implement an **MQTT network** for real-time robotic hand control.
- Optimize the classifier for **faster and more accurate recognition**.

---

## **🛠️ Customizing for Your Own Gestures**
Want to add a new gesture?  
1. **Edit `gesture_data_collection.py`** and add a new key in `gesture_data`:
   ```python
   gesture_data = {
       "thumbs_up": [],
       "fist": [],
       "open_palm": [],
       "peace_sign": []  # 👈 Add a new gesture
   }
   ```
2. Modify the key press mapping:
   ```python
   if key == ord("p"):  # Press "P" for peace sign
       gesture_data["peace_sign"].append(keypoints)
       print("Saved Peace Sign Gesture")
   ```
3. Train the model again:
   ```bash
   python gesture_trainer.py
   ```
4. Run live recognition:
   ```bash
   python Webcam_Gesture.py
   ```

---

## **📌 File Structure**
```
Hand-Gesture-KNN/
│── gesture_data_collection.py  # Collects hand gestures via webcam
│── gesture_trainer.py          # Trains the KNN model
│── Webcam_Gesture.py           # Runs real-time gesture recognition
│── gesture_data.pkl            # Stores recorded gesture data
│── gesture_classifier.pkl      # Trained KNN model
│── requirements.txt            # Dependencies list
│── README.md                   # Documentation
```

---

## **🤝 Contributing**
This is an **open-source project**!  
🔹 Feel free to **add new gestures, improve accuracy, or integrate with hardware**.  
🔹 If you create an adaptation (e.g., **robotic hand control**), consider contributing back!

---

## **📄 License**
This project is licensed under the **MIT License**. You are free to modify and use it in your own projects.

---

## **📬 Contact & Feedback**
Got ideas? Want to contribute? Open an issue or pull request!  

📧 **Email:** [Your Email]  
💡 **GitHub:** [Your GitHub Profile]  

🚀 **Happy coding, and let’s build the future of assistive technology together!** 🚀

---

### **🔥 Summary**
✅ **Fully customizable gesture training system**  
✅ **Trains and classifies gestures using KNN**  
✅ **Designed for future prosthetic hand control**  
✅ **Open-source and easy to extend** 
