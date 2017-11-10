import requests  
import json  
import time  
  
def main():  
    fileRecord = open("result.txt", "w")  
    fileRecord.write("connect to yeelink\n");  
    fileRecord.close()  
    while True:  
       
        file = open("/sys/class/thermal/thermal_zone0/temp")  
        
        temp = float(file.read()) / 1000  
        
        file.close()  
  
       
        apiurl = 'http://api.yeelink.net/v1.1/device/353401/sensor/398757/datapoints'  
        
        apiheaders = {'U-ApiKey': '0e0e7e612f2df9d07663c1e506f58886', 'content-type': 'application/json'}  
         
        payload = {'value': temp}  
        
        r = requests.post(apiurl, headers=apiheaders, data=json.dumps(payload))  
  
       
        fileRecord = open("result.txt", "a")  
        strTime = time.strftime('%Y-%m-%d:%H-%M-%S',time.localtime(time.time()))  
        fileRecord.writelines(strTime + "\n")  
        strTemp = "temp : %.1f" %temp + "\n"  
        fileRecord.writelines(strTemp)  
        fileRecord.writelines(str(r.status_code) + "\n")  
        fileRecord.close()  
          
        time.sleep(20)  
  
for i in range(10):
    main()#upload data every 20 seconds, total 10 times
