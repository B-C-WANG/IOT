import requests  
import json  
import time  
  
 
import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
time.sleep(1)

def get_data():
           while 1:

                r=1
                time.sleep(0.5)
                j=0

                gpio.setup(12,gpio.OUT)
                gpio.output(12,gpio.LOW)
                time.sleep(0.02)
                gpio.output(12,gpio.HIGH)
                gpio.setup(12,gpio.IN)
                i=1
                while gpio.input(12)==0:
                    continue
                 
                while gpio.input(12)==1:
                        continue
                data=[]
                j=0
                r=1
                while r<2500:
                        

                            data.append(gpio.input(12))
                            r+=1

                result=[]
                r=0
                for i in range(len(data)-1):     
                        if data[i]==data[i+1]:
                           r+=1
                        else:
                                   result.append(r)
                                   r=0
                #print result,len(result)
                # !!!the len(result) must be 81! the 80 data we will need
                data=[]
                
                if len(result)==81:
                
                        for i in range(0,40):
                                        if result[2*i]>result[2*i+1]:
                                                data.append(0)
                                        else:
                                                data.append(1)

                
                

                        print len(data)
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

                                #print "temperature is ", temperature,"wet is ",humidity,"%"
                                return humidity,temperature
                        else:
                                        print 'wrong'
                                        get_data()#if wrong , go again
                                




  
def main(humi,tem):  
    
      
       
        humi=humi
        tem=tem
  
       
        apiurl1 = 'http://api.yeelink.net/v1.1/device/353401/sensor/398745/datapoints'  
        
        apiheaders = {'U-ApiKey': '0e0e7e612f2df9d07663c1e506f58886', 'content-type': 'application/json'}  
         
        payload1 = {'value': tem}  
        
        r = requests.post(apiurl1, headers=apiheaders, data=json.dumps(payload1))  

        apiurl2 = 'http://api.yeelink.net/v1.1/device/353401/sensor/398759/datapoints'

        payload2 = {'value': humi}  
        
        r = requests.post(apiurl2, headers=apiheaders, data=json.dumps(payload2))
        
       
    
          
        time.sleep(1)  
  
for i in range(10):
        humi,tem=get_data()
        main(humi,tem)#upload data every 1~5 seconds, total 10 times


#sometimes the len of result will be wrong, dont know why

