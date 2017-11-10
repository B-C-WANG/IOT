import struct
mou=open('/dev/input/mice',"rb")

def m_event():
    m=mou.read(3)
    
    b=ord(m[0])
    bl=b& 0x1
    bm=(b&0x4)> 0
    br=(b&0x2)>0
    x,y=struct.unpack("bb",m[1:])
    print bl,bm,br,x,y
while 1:
    m_event()
    
mou.close()
         
