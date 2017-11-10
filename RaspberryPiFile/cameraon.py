import io
import time
import picamera
import cv2
import numpy as np



def camera():
    # Create the in-memory stream
        with picamera.PiCamera() as camera:
            camera.start_preview()
            time.sleep(10000)

camera()
