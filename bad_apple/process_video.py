import cv2
import numpy as np

video_path = 'bad_apple.mp4'

capture = cv2.VideoCapture(video_path)

scale_factor = 8

target_resolution = (4 * scale_factor, 3 * scale_factor)

frames_data = []

while capture.isOpened():
    ret, frame = capture.read()
    if not ret:
        break 
    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    resized_frame = cv2.resize(gray_frame, target_resolution)
    
    frames_data.append(resized_frame)

capture.release()

frames_data = np.array(frames_data)

print(f"Processed {frames_data.shape[0]} frames with resolution {target_resolution}")

np.savez_compressed(f'{target_resolution}_video.npz', frames=frames_data)