#ctrl the 16 out 1 or 0 by mouse leftclick or right click
#if left click then blink 1 second , if right click then blink 0.2 second.
import RPi.GPIO as io
import time
import random
import struct
io.setmode(io.BCM)
io.cleanup()
io.setup(16,io.OUT)
#for i in range(10):
#    io.output(16,1)
#    print 1
#    time.sleep(0.5)
#    io.output(16,0)
#    time.sleep(0.5)

mou=open('/dev/input/mice',"rb")

def m_event():
    m=mou.read(3)
    
    b=ord(m[0])
    bl=b& 0x1
    
    br=(b&0x2)>0
    return bl,br
    
    
while 1:
    bl,br=m_event()
    
    if bl==1:
        
        
           io.output(16,1)
           time.sleep(0.05)
           io.output(16,0)
           
    if br==1:
        io.output(16,1)
        time.sleep(1)
        io.output(16,0)
        
        
    
mou.close()
io.cleanup()
