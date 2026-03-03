import os
import time
import threading
from ultralytics import YOLO
from gtts import gTTS
from playsound import playsound

is_speaking = False

# 1. Setup Audio Function (Threaded/Non-blocking)
def play_audio_task(text):
    global is_speaking
    try:
        is_speaking = True  # Set the lock
        tts = gTTS(text=text, lang='en')
        filename = f"voice_{int(time.time())}.mp3"
        tts.save(filename)
        playsound(filename)
        if os.path.exists(filename):
            os.remove(filename)
    except Exception as e:
        print(f"Audio Error: {e}")
    finally:
        is_speaking = False  # Release the lock when finished

def speak(text):
    global is_speaking

    if not is_speaking:
        threading.Thread(target=play_audio_task, args=(text,), daemon=True).start()

# 2. Initialize Model
# Make sure best.pt is in the same folder as this script
model = YOLO('best.pt') 

# 3. State Trackers
last_message = ""
last_speech_time = 0
cooldown_period = 4  # Seconds to wait before repeating the same info

# 4. Main Detection Loop
# source=0 opens your webcam
results = model.predict(source=0, show=True, conf=0.25, stream=True)

print("Starting The Intelligent Eye... Press 'q' in the camera window to stop.")

for r in results:
    current_time = time.time()
    
    if len(r.boxes) > 0:
        img_width = r.orig_shape[1]
        
        # Prioritize the largest (closest) traffic light
        best_box = max(r.boxes, key=lambda b: b.xywh[0][2] * b.xywh[0][3])
        
        label = model.names[int(best_box.cls[0])]
        center_x = best_box.xywh[0][0].item()

        # Directional Logic
        if center_x < img_width / 3:
            direction = "on your left"
        elif center_x > (2 * img_width) / 3:
            direction = "on your right"
        else:
            direction = "straight ahead"

        message = f"{label} light {direction}"

        # Logic: Speak only if the situation changed OR 4 seconds have passed
        time_since_last_speech = current_time - last_speech_time
        
        if message != last_message or time_since_last_speech > cooldown_period:
            print(f"ACTION: {message}")
            speak(message)
            last_message = message
            last_speech_time = current_time
    else:
        # If nothing is detected, we reset last_message so it speaks immediately 
        # when a light reappears.
        if last_message != "":
            print("Path clear: No lights detected.")
            last_message = ""