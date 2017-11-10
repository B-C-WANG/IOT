from PIL import Image,ImageDraw
import picamera
import time
camera=picamera.PiCamera()
try:
    camera.start_preview()
    time.sleep(5)
    camera.stop_preview()
finally:
    camera.close()
im=Image.open('123.jpg')
data=(0,255,255)
pic=ImageDraw.Draw(im)
for i in range(50):
    for j in range(50):
        point=[i,j]
        pic.point(point,data)
im.save('out.jpg')

print 'done'
