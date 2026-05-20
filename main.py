import os
import time
import threading
from ultralytics import YOLO
from gtts import gTTS
from playsound import playsound

is_speaking = False


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
        is_speaking = False  
def speak(text):
    global is_speaking

    if not is_speaking:
        threading.Thread(target=play_audio_task, args=(text,), daemon=True).start()


model = YOLO('best.pt') 


last_message = ""
last_speech_time = 0
cooldown_period = 4  



results = model.predict(source=0, show=True, conf=0.25, stream=True)

print("Starting The Intelligent Eye... Press 'q' in the camera window to stop.")

for r in results:
    current_time = time.time()
    
    if len(r.boxes) > 0:
        img_width = r.orig_shape[1]
        
        best_box = max(r.boxes, key=lambda b: b.xywh[0][2] * b.xywh[0][3])
        
        label = model.names[int(best_box.cls[0])]
        center_x = best_box.xywh[0][0].item()

        
        if center_x < img_width / 3:
            direction = "on your left"
        elif center_x > (2 * img_width) / 3:
            direction = "on your right"
        else:
            direction = "straight ahead"

        message = f"{label} light {direction}"

     
        time_since_last_speech = current_time - last_speech_time
        
        if message != last_message or time_since_last_speech > cooldown_period:
            print(f"ACTION: {message}")
            speak(message)
            last_message = message
            last_speech_time = current_time
    else:
        
       
        if last_message != "":
            print("Path clear: No lights detected.")
            last_message = ""
