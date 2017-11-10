import serial
ser=serial.Serial('/dev/ttyUSB0',9600,timeout=1)
ser.close()#deal with the warning: ser have been opend
ser.open()


temp=input('insert a')
temp1=input('insert b')
while 1:
    temp2=input('1:add,2:minus,3:mul,4:div')
    if temp2  in [1,2,3,4]:
        break 
    
print type(temp)
ser.write(temp)
ser.write(temp1)
ser.write(temp2)

try:
    while 1:
        print 'success'
        response=ser.readline()
except:
    print 'task have  not finished '
    ser.close()
