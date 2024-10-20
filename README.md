# Intrusion-Detection-System
This project demonstrates a simple Intrusion Detection System (IDS) using OpenCV and Pose Detection. The system detects human presence in real-time through a webcam feed and sends an SMS alert when an intrusion is detected. The SMS notification is triggered when a human is continuously detected for a certain period, ensuring that the detection is not due to false positives.

## Features
- Real-time pose detection using the webcam feed.
- SMS alerts when human presence is detected continuously.
- Pose detection powered by `cvzone` and `OpenCV`.

## Project Structure

- `IDS.py`: Contains the core logic for pose detection and triggering the SMS alert.
- `send.py`: Handles the sending of SMS alerts (this requires a service like Twilio to be set up).

## How It Works
1. The webcam captures video input.
2. Pose detection is applied using the `cvzone.PoseModule`.
3. If a human is detected continuously for 50 frames, an SMS alert is sent via a messaging service (such as Twilio).
4. The system stops sending further SMS alerts after the first one unless restarted.

## Requirements

1. Python 3.x
2. OpenCV
3. cvzone (for pose detection)
4. A messaging service (e.g., Twilio) to send SMS alerts.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/intrusion-detection-pose-sms.git
   ```

2. Install the required dependencies:
   ```bash
   pip install opencv-python
   pip install cvzone
   ```

3. Set up SMS sending service in `send.py` (for example, using Twilio).

## Usage

1. Run the project:
   ```bash
   python main.py
   ```

2. The webcam feed will open, and human detection will begin. If a human is detected for more than 50 frames, an SMS alert will be sent.

3. To quit, press the **`q`** key.

## Acknowledgments
- [OpenCV](https://opencv.org/) for computer vision.
- [cvzone](https://github.com/cvzone/cvzone) for pose detection.
- [Twilio](https://www.twilio.com/) (or any SMS service) for sending SMS alerts.

---

Feel free to adjust the file as needed.
