# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 14:24:43 2014
 
@author: pi
"""
 
import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
time.sleep(1)
data=[]
def delay(i): #20*i usdelay
    a=0
    for j in range(i):
        a+1
j=0
#start work
gpio.setup(12,gpio.OUT)
#gpio.output(12,gpio.HIGH)
#delay(10)
gpio.output(12,gpio.LOW)
time.sleep(0.02)
gpio.output(12,gpio.HIGH)
i=1
  
#wait to response
gpio.setup(12,gpio.IN)
 
 
while gpio.input(12)==1:
    continue
 
 
while gpio.input(12)==0:
    continue
 
while gpio.input(12)==1:
        continue
#get data
 
while j<40:
    k=0
    while gpio.input(12)==0:
        continue
     
    while gpio.input(12)==1:
        k+=1
        if k>100:break
    if k<3:
        data.append(0)
    else:
        data.append(1)
    j+=1
 
print "Sensor is working"
print data
#get temperature
humidity_bit=data[0:8]
humidity_point_bit=data[8:16]
temperature_bit=data[16:24]
temperature_point_bit=data[24:32]
check_bit=data[32:40]
 
humidity=0
humidity_point=0
temperature=0
temperature_point=0
check=0
 
 
 
for i in range(8):
    humidity+=humidity_bit[i]*2**(7-i)
    humidity_point+=humidity_point_bit[i]*2**(7-i)
    temperature+=temperature_bit[i]*2**(7-i)
    temperature_point+=temperature_point_bit[i]*2**(7-i)
    check+=check_bit[i]*2**(7-i)
 
tmp=humidity+humidity_point+temperature+temperature_point
if check==tmp:
    print "temperature is ", temperature,"wet is ",humidity,"%"
else:
    print "something is worong the humidity,humidity_point,temperature,temperature_point,check is",humidity,humidity_point,temperature,temperature_point,check
