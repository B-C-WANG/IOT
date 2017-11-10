import serial
ser=serial.Serial('/dev/ttyUSB0',9600,timeout=1)
ser.close()#deal with the warning: ser have been opend
ser.open()


temp='2'
temp1='4'
temp2='3'
ser.write(temp)
ser.write(temp1)
ser.write(temp2)

try:
    while 1:
        ser.write('111')
        print 'success'
        response=ser.readline()
        print response
except:
    print 'task have  not finished '
    ser.close()
