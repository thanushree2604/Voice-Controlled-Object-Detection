# 🎤 Voice Controlled Object Detection

## 🧩 Overview
**Voice Controlled Object Detection** is an AI project that allows users to control and trigger real-time object detection using **voice commands**.
It combines **speech recognition** with **computer vision (YOLOv8)** to create a hands-free, interactive system for identifying objects through a webcam or video feed.

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/voice-object-detection.git
   cd voice-object-detection
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   *(If you don’t have `requirements.txt`, install manually:)*
   ```bash
   pip install opencv-python ultralytics SpeechRecognition pyttsx3 pyaudio
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

---

## 🗣️ How It Works

1. The system greets and waits for your **voice command**.
2. You can say an object name, e.g.,
   > “Detect person” or “Find car”
3. YOLOv8 processes the webcam feed to identify the object.
4. When the target object is found, it displays a **“DETECTED”** message on the frame and provides a **spoken confirmation**.
5. Say **“exit”** or press **Q** to stop detection.

---

## 🧪 Supported Voice Commands

| Command          | Action                      |
| ---------------- | --------------------------- |
| “Detect person”  | Detects people              |
| “Find dog”       | Detects dogs                |
| “Exit” or “Quit” | Stops the program           |
| “Stop detection” | Ends current detection loop |

---

## 🧑‍💻 Author

**Thanushree N S**  
💡 AI & Computer Vision Enthusiast  
🔗 [GitHub Profile](https://github.com/thanushree2604)

---

## 📜 License

This project is licensed under the **MIT License** — you are free to use, modify, and distribute it.

---

## ❤️ Acknowledgments

* [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
* [SpeechRecognition Library](https://pypi.org/project/SpeechRecognition/)
* [OpenCV](https://opencv.org/)
* [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/)
