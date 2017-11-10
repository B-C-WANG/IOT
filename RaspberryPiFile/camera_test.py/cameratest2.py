import io
import time
import picamera
import cv2
import numpy as np



def camera(sleeptime,totaltime,r,g,b):
    # Create the in-memory stream
    for i in range(totaltime):
        stream = io.BytesIO()
        with picamera.PiCamera() as camera:
            camera.start_preview()
            time.sleep(sleeptime)
            camera.capture(stream, format='jpeg')
        # Construct a numpy array from the stream
        data = np.fromstring(stream.getvalue(), dtype=np.uint8)
        # "Decode" the image from the array, preserving colour
        image = cv2.imdecode(data, 1)
        # OpenCV returns an array with data in BGR order. If you want RGB instead
        # use the following...
        image = image[:, :, ::-1]
     
        for i in range(480):
            for j in range(848):
                    if image[i][j][0] <r and image[i][j][1] <g and image[i][j][2] <b:

                            return (i,j)
                    else:
                        pass

for i in range(500):
    print camera(0.5,500,100,100,100)
#this programme is used to detect where is blank, you can use a black paper
    # see if it can track your black paper,
    #then use it to track yourself.
