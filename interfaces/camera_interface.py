import cv2
import time
from typing import Optional, Tuple
import numpy as np

class CameraInterface:
    def __init__(self, source=0, width=1280, height=720, fps=30):
        self.source = source
        self.cap = cv2.VideoCapture(source)
        self.frame_count = 0
        self.fps = 0
        self.start_time = time.time()
        
        # Set camera properties
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.cap.set(cv2.CAP_PROP_FPS, fps)
        
        if not self.cap.isOpened():
            raise ValueError(f"Could not open video source: {source}")
    
    def get_frame(self) -> Tuple[bool, Optional[np.ndarray]]:
        """Get next frame from video source"""
        ret, frame = self.cap.read()
        
        if ret:
            self.frame_count += 1
            # Calculate FPS every 30 frames
            if self.frame_count % 30 == 0:
                self.fps = 30 / (time.time() - self.start_time)
                self.start_time = time.time()
        
        return ret, frame
    
    def get_fps(self) -> float:
        """Get current FPS"""
        return self.fps
    
    def release(self):
        """Release video capture"""
        self.cap.release()
    
    def __del__(self):
        self.release()