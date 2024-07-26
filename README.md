# Object Trajectory Prediction using Kalman Filter

This code demonstrates the detection of a fruit object in a video and the prediction of its trajectory using a Kalman filter. The implementation utilizes OpenCV for video processing, and custom modules for object detection and Kalman filtering.

## Features
- **Orange Object Detection**: Detects the orange object in each video frame.
- **Trajectory Prediction**: A Kalman filter is used to predict the future position of the detected orange object.
- **Visualization**: Displays the video with annotations showing the detected and predicted positions of the object.

## Requirements

- Python 3.9
- OpenCV (`cv2`)
- Custom modules: `orange_detector`, `kalmanfilter`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AlirezaHabibi1377/Object-Trajectory-Prediction-using-Kalman-Filter.git
