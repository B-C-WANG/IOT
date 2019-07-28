#include <SPI.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BMP280.h>
#define BMP_SCK 5
#define BMP_MISO 8
#define BMP_MOSI 10
#define BMP_CS 9
File myFile;//文件
unsigned long starttime;
unsigned long stoptime;//用来表示时间的变量
Adafruit_BMP280 bme(BMP_CS, BMP_MOSI, BMP_MISO,  BMP_SCK);
void setup() {
myFile = SD.open("test.txt", FILE_WRITE);//文件名设置
 myFile.println(',');
 myFile.close();//这里一开始就打印一个换行，是为了重插电后便于区分，打印内容不重要
  Serial.begin(9600);
  starttime=millis();
  while (!Serial) {
    ; 
  }
if (!SD.begin(4)) {
    Serial.println("initialization failed!");//sd卡模块报错
    return;
  }
  Serial.print("Initializing ...");
  if (!bme.begin()) {  
    Serial.println("Could not find a valid BMP280 sensor, check wiring!");//bmp280报错  
    while (1);
  }
} 
void loop() {
  myFile = SD.open("test.txt", FILE_WRITE);
   Serial.print("Temperature = ");
   Serial.print(bme.readTemperature());
   Serial.println(" *C");
   Serial.print("Pressure = ");
   Serial.print(bme.readPressure());
   Serial.println(" Pa");
   Serial.print(stoptime-starttime);
   Serial.print(',');
   Serial.print("Writing to test.txt...");//上面是串口数据的打印，只是采集的话可以删去
    stoptime=millis();
    myFile.print(stoptime-starttime);//时间序列的存储，需要自己记一下开始时间推算
    myFile.print(',');
    myFile.print(bme.readTemperature());
    myFile.print(',');
    myFile.print(bme.readPressure());
    myFile.print(',');
    delay(1000);//改变测量时间间隔
    myFile.close();
    Serial.println("done.");//这里删去了高度数据，需要的话可以基于原来的代码改
