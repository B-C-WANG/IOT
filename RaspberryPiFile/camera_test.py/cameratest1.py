import io
import time
import picamera
import cv2
import numpy as np

# Create the in-memory stream
stream = io.BytesIO()
with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(0.01)
    camera.capture(stream, format='jpeg')
# Construct a numpy array from the stream
data = np.fromstring(stream.getvalue(), dtype=np.uint8)
# "Decode" the image from the array, preserving colour
image = cv2.imdecode(data, 1)
# OpenCV returns an array with data in BGR order. If you want RGB instead
# use the following...
image = image[:, :, ::-1]

print image
print type(image)
temp=image.shape
print temp
data=[]
que=0
for i in range(temp[0]):
    for j in range(temp[1]):
        a=image[i][j]
        print a
        data.append(a)
        
        
print data
print 'end'







        


file=open('123.txt','w')
file.write(image)
