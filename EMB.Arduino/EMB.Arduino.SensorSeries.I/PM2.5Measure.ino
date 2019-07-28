#include <SD.h>
#include <Wire.h>
#include <SPI.h>
#include <stdlib.h>
int dustPin=0;
int ledPower=2;
int delayTime=280;
int delayTime2=40;
float offTime=9680;
File myFile;
unsigned long starttime;
unsigned long stoptime;
int dustVal=0;
int i=0;
float ppm=0;
char s[32];
float voltage = 0;
float dustdensity = 0;
float ppmpercf = 0;
void setup(){
   starttime=millis();
  while (!Serial) {  ; 
  }
if (!SD.begin(4)) {
    Serial.println("initialization failed!");
    return;
  }
 myFile = SD.open("pm25.txt", FILE_WRITE);
 myFile.println(',,,,,');
 myFile.close();
Serial.begin(9600);
pinMode(ledPower,OUTPUT);
delay(1000);//等待setup
i=0;
ppm =0;
}
void loop(){
myFile = SD.open("pm25.txt", FILE_WRITE);
i=i+1;
digitalWrite(ledPower,LOW); // power on the LED
delayMicroseconds(delayTime);
dustVal=analogRead(dustPin); // read the dust value
ppm = ppm+dustVal;
delayMicroseconds(delayTime2);
digitalWrite(ledPower,HIGH); // turn the LED off
delayMicroseconds(offTime);
voltage = ppm/i*0.0049;
dustdensity = 0.17*voltage-0.1;
ppmpercf = (voltage-0.0256)*120000;
if (ppmpercf < 0)
ppmpercf = 0;
if (dustdensity < 0 )
dustdensity = 0;
if (dustdensity > 0.5)
dustdensity = 0.5;
String dataString = "";
dataString += dtostrf(voltage, 9, 4, s);
dataString += ",";
dataString += dtostrf(dustdensity, 5, 2, s);
dataString += ",";
dataString += dtostrf(ppmpercf, 8, 0, s);
i=0;
ppm=0;
Serial.println(dataString);
stoptime=millis();
 myFile.print(stoptime-starttime);
    myFile.print(',');
    myFile.print(dataString);
    myFile.print(',');
    delay(500);//设置周期
     myFile.close();
    Serial.println("done."); 
}
