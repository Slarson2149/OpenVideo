from flask import Flask, request
import cv2

app = Flask(__name__)

@app.route('/video_feed')
def video_feed():
    """
    This route handles the video feed from the client.
    """
    # Get the video frame from the client
    video_frame = request.data
    # Decode the video frame
    decoded_frame = cv2.imdecode(np.frombuffer(video_frame, np.uint8), -1)
    # Save the video frame to a specified path
    cv2.imwrite("path/to/save/video/frame.jpg", decoded_frame)
    return "OK"

@app.route('/text_message', methods=['POST'])
def text_message():
    """
    This route handles text messages from the client.
    """
    # Get the text message from the client
    message = request.form['message']
    print(message)
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
