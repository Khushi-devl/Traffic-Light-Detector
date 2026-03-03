The Intelligent Eye: AI-Powered Navigation Aid
The Intelligent Eye is a computer vision project designed to assist visually impaired individuals by detecting obstacles—specifically traffic lights—in real-time and providing descriptive audio feedback.

🚀 Key Features
Real-time Detection: Utilizes the YOLOv8 Nano architecture for high-speed object detection on edge devices.

Audio Alerts: Integrated with pyttsx3 to provide voice notifications when a specific object (like a traffic light) is detected.

CPU Optimized: Configured with a reduced image size (imgsz=320) to ensure smooth performance on standard laptops without a dedicated GPU.

Privacy Control: Includes a camera toggle feature to enable or disable the video feed during operation.

🛠️ Architecture
The project follows a Deep Learning Pipeline for Computer Vision:

Model: YOLOv8n (Nano).

Backbone: Modified CSPDarknet53 using C2f modules for efficient feature extraction.

Head: Decoupled, anchor-free detection head for precise classification and localization.

Dataset: Custom "traffic-light-v9orl" dataset curated and versioned via Roboflow.

📦 Requirements
To run this project locally, you will need:

Bash
pip install ultralytics pyttsx3 opencv-python numpy
💻 How to Run
Ensure your trained model weights (best.pt) are in the project directory.

Run the main script:

Bash
python main.py
Controls:

Press 'c' to toggle (enable/disable) the camera.

Press 'q' to quit the application safely.

I am a B.Tech Information Technology student (4th Semester) with a passion for building AI solutions that solve real-world problems. The Intelligent Eye represents my journey into Deep Learning, specifically focusing on Computer Vision and accessible technology.
