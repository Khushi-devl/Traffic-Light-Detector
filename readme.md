🚦 Traffic Light Detector using YOLOv8
This project is a real-time Traffic Light Detection and Classification system developed using the YOLOv8 (You Only Look Once) architecture. The model is trained to identify traffic light states and can be integrated into autonomous vehicle systems or smart city infrastructure.

🌟 Features
Real-time Detection: High-speed processing using the lightweight YOLOv8 model.

State Classification: Detects Red, Green, and Yellow lights.

Voice Feedback: Includes audio cues for detected states (Red/Green/Yellow).

Pre-trained Weights: Includes the custom-trained best.pt model file.

📁 Project Structure
main.py: The primary script to run the detection system.

best.pt: The optimized YOLOv8 weights after training.

voice/: Folder containing audio files for voice notifications.

dataset/: Training data sourced via Roboflow.

🛠️ Requirements
To run this project, you need the following dependencies:

🚀 How to Run
Clone the repository:

Navigate to the project folder:

Run the detector:

📊 Dataset
The dataset was exported from Roboflow and includes pre-processed images of various traffic light conditions.