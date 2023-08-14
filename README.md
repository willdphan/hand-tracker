# Hand Tracker

## Overview

The provided code uses the mediapipe library to detect and track hands in real-time through the camera feed. The hand detection includes identifying key landmarks on the hands and drawing them onto the image feed. The program calculates and displays the frames per second (FPS) for performance monitoring.

## Features

Hand Detector Class:

Organized for easier reuse and integration into other projects.
Detects hands and draws the landmarks and connections.
Retrieves the specific position of any landmark on the detected hands.
Real-time FPS Calculation:

Monitor performance and processing speed.

[Module](/Users/williamphan/Desktop/hand-tracker/hand-tracker-module.py)

Simple Script:

A basic version that captures the video feed and detects hands without the need for a class structure.

[Script](/Users/williamphan/Desktop/hand-tracker/hand-tracker.py) <br/>

## Usage

Install the required libraries:

`pip install opencv-python mediapipe`

Run the scripts

`python <hand-tracker-module.py>.py`
`python <hand-tracker.py>.py`

---

## Note

Ensure you have a working camera and the necessary permissions are granted to access the camera feed. Adjust
`cap = cv2.VideoCapture(0)` parameter depending on which camera you want to use.

---

## License

This script is open-source and licensed under the MIT License. For more details, check the [LICENSE](LICENSE) file.
