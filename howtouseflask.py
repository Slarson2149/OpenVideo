import requests
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        # Encode the video frame
        _, encoded_frame = cv2.imencode('.jpg', frame)
        # Send the video frame to the server
        requests.post("http://server_ip:5000/video_feed", data=encoded_frame.tostring())
