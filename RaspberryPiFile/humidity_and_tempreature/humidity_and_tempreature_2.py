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

def get_data():
    #get data
        r=1

        
        time.sleep(0.5)
        j=0
        #start work
        
        #gpio.output(12,gpio.HIGH)
        #delay(10)
        gpio.setup(12,gpio.OUT)
        gpio.output(12,gpio.LOW)
        time.sleep(0.02)
        gpio.output(12,gpio.HIGH)
        gpio.setup(12,gpio.IN)
        i=1
        #wait to response
        
         
         
        #while gpio.input(12)==1:
        #    continue
         
         
        while gpio.input(12)==0:
            continue
         
        while gpio.input(12)==1:
                continue
        data=[]
        j=0
        r=1
        while r<2500:#why i set 2000 here? to ensure the sensor send data over!
                

                    data.append(gpio.input(12))#!!according to the api, when;
#;send data over,result will always be 1
                    #time.sleep(0.02)#api give that 0 is 50us low and 27us high,
                    # and 1 is 50us low and 70us high
                    r+=1
                

            #print "Sensor is working"
        print data
        return data

def the_0_1_data(list):
        result=[]
        r=0
        for i in range(len(list)-1):     
                if list[i]==list[i+1]:
                   r+=1
                else:
                           result.append(r)
                           r=0
        print result,len(result)
        # !!!the len(result) must be 81! the 80 data we will need
        data=[]
        #the first one is the numbers of 0 ,which is the singal
        #to show "we are going to send you data", rather than data we need
        for i in range(0,40):
                if result[2*i]>result[2*i+1]:
                        data.append(0)
                else:
                        data.append(1)

        print data,len(data)
        return data
        

def data_final_deal(list):
        #get temperature
    data=list
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
            
        print humidity,temperature,check
        print "temperature is ", temperature,"wet is ",humidity,"%"
        return humidity,temperature
        #else:
        #    print "something is worong the humidity,humidity_point,temperature,temperature_point,check is",humidity,humidity_point,temperature,temperature_point,check


data_final_deal(the_0_1_data(get_data()))





