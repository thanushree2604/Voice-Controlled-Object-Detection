import cv2
import speech_recognition as sr
import pyttsx3
from ultralytics import YOLO
import time

# Initialize text-to-speech
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    print("🤖:", text)
    engine.say(text)
    engine.runAndWait()

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening for your command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"🎤 You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn’t catch that.")
        return ""
    except sr.RequestError:
        speak("Speech service unavailable.")
        return ""

def extract_target_object(command):
    objects = ["person", "car", "dog", "cat", "bottle", "cell phone", "laptop", "chair"]
    for obj in objects:
        if obj in command:
            return obj
    return None

def main():
    speak("Voice controlled object detection system activated.")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        speak("Error: Cannot access the webcam.")
        print("❌ Webcam not opening. Try changing the camera index to 1 or 2.")
        return

    while True:
        command = listen_command()
        if "exit" in command or "quit" in command:
            speak("Exiting program. Goodbye!")
            break

        target = extract_target_object(command)
        if not target:
            speak("Please specify an object to detect, like person or dog.")
            continue

        speak(f"Detecting {target}. Press Q to stop detection.")
        time.sleep(1)

        while True:
            ret, frame = cap.read()
            if not ret:
                speak("Failed to read from webcam.")
                break

            results = model(frame, verbose=False)
            annotated_frame = results[0].plot()

            names = results[0].names
            detected = [names[int(cls)] for cls in results[0].boxes.cls]

            if target in detected:
                cv2.putText(annotated_frame, f"{target.upper()} DETECTED!", (30, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
                speak(f"{target} detected!")
                cv2.imshow("Voice Controlled Object Detection", annotated_frame)
                cv2.waitKey(2000)
                break

            cv2.imshow("Voice Controlled Object Detection", annotated_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                speak("Stopped detection.")
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
