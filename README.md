# 🎤 Voice Controlled Object Detection

## 🧩 Overview
**Voice Controlled Object Detection** is a Python-based AI project that combines **speech recognition** and **YOLOv8** computer vision for real-time, voice-controlled object detection.  
You can simply **speak the object name** (like *person*, *dog*, or *car*), and the system will automatically detect and announce it through your webcam feed — completely hands-free.

---

## 🚀 Features
- 🎙️ Voice commands to control detection  
- 🧠 Real-time object recognition using **YOLOv8**  
- 🔊 Text-to-speech feedback via `pyttsx3`  
- 📷 Webcam-based live detection  
- 🛑 Voice or keypress-based exit  
- 💡 Supports common objects (person, car, dog, cat, bottle, etc.)

---

## 🧰 Technologies Used
- **Python 3.8+**
- **OpenCV** – for video capture and display  
- **Ultralytics YOLOv8** – for deep-learning object detection  
- **SpeechRecognition** – for voice command processing  
- **PyAudio** – for microphone input  
- **pyttsx3** – for text-to-speech feedback  

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/thanushree2604/Voice-Controlled-Object-Detection.git
   cd Voice-Controlled-Object-Detection
````

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

---

```

Would you like me to also generate a `requirements.txt` file for this project (based on the imports in `main.py`)?
```
