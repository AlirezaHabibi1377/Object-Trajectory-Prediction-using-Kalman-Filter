import cv2
from orange_detector import OrangeDetector
from kalmanfilter import KalmanFilter

# Open the video file
cap = cv2.VideoCapture("orange.mp4")

# Initialize the OrangeDetector for detecting oranges
od = OrangeDetector()

# Initialize the KalmanFilter for predicting the trajectory of the orange
kf = KalmanFilter()

while True:
    # Read a frame from the video
    ret, frame = cap.read()
    if ret is False:
        break # Break the loop if no more frames are available

    # Detect the orange in the current frame and get its bounding box
    orange_bbox = od.detect(frame)
    x, y, x2, y2 = orange_bbox

    # Calculate the center coordinates of the detected orange
    cx = int((x + x2) / 2)
    cy = int((y + y2) / 2)

    # Predict the next position of the orange using the Kalman filter
    predicted = kf.predict(cx, cy)

    # Draw a circle at the current center of the detected orange
    cv2.circle(frame, (cx, cy), 20, (0, 0, 255), 4)

    # Draw a circle at the predicted position of the orange
    cv2.circle(frame, (predicted[0], predicted[1]), 20, (255, 0, 0), 4)

    # Display the frame with the detected and predicted positions
    cv2.imshow("Frame", frame)

    # Wait for 150 milliseconds and check if the 'Esc' key is pressed
    key = cv2.waitKey(150)
    if key == 27: # ASCII code for the 'Esc' key
        break # Break the loop if the 'Esc' key is pressed


# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
