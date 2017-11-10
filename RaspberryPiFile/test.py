import serial
import RPi.GPIO
import time
ser= serial.Serial('/dev/ttyUSB0',9600,timeout=1)
ser.close()
ser.open()
#time.sleep(1)#wait to test
time.sleep(3)
ser.write(str('testing'))
while 1:
    
    response=ser.readall()
    print response
