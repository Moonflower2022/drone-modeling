import cv2
import numpy as np
from process_video import target_resolution

data = np.load(f'{target_resolution}_video.npz')

frames_data = data['frames']

fps = 30 

scale_factor = 30

for frame in frames_data:
    frame = frame.astype(np.uint8)

    larger_frame = cv2.resize(frame, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_NEAREST)
    
    cv2.imshow('Video from npz', larger_frame)
    
    if cv2.waitKey(int(1000 / fps)) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()