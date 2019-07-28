//

#include <SD.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <SPI.h>
 

#define ONE_WIRE_BUS 2
//Two Onewire Tenperature Sensor plug in the same 2 pin.
//把两个温度sensor线插在同一个2号口中
 

OneWire oneWire(ONE_WIRE_BUS);

DallasTemperature sensors(&oneWire);
 File myFile;
 File myFile_2;
unsigned long starttime;
    unsigned long stoptime;
void setup()
{

  Serial.begin(9600);
  Serial.println("Dallas Temperature IC Control Library Demo");
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }
if (!SD.begin(4)) {
    Serial.println("initialization failed!");
    return;
  }
   Serial.print("Initializing ...");
   myFile = SD.open("temp.txt", FILE_WRITE);
 myFile.println(',,,,,');
 myFile.close();
 myFile_2 = SD.open("temp2.txt", FILE_WRITE);
 myFile_2.println(',,,,,');
 myFile_2.close();
 
  sensors.begin();
  starttime=millis();
}
 
void loop(void)
{ 
  myFile = SD.open("temp.txt", FILE_WRITE);
  myFile_2 = SD.open("temp2.txt", FILE_WRITE);

  sensors.requestTemperatures(); 
  
  
  Serial.println(sensors.getTempCByIndex(0));  
  stoptime=millis();
 myFile.print(stoptime-starttime);
    myFile.print(',');
    myFile.print(sensors.getTempCByIndex(0));
    myFile.print(',');
    
    
    Serial.println(sensors.getTempCByIndex(1));  
  stoptime=millis();
 myFile_2.print(stoptime-starttime);
    myFile_2.print(',');
    myFile_2.print(sensors.getTempCByIndex(1));
    myFile_2.print(',');
    
    
   delay(500);
    myFile.close();
    myFile_2.close();
}
