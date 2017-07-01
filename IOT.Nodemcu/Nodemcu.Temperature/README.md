# IOT.NodeMcu.Temperature
**实现了利用nodemcu以及Python数据处理进行的wifi的局域网远程温度测量**

## 准备
 - 采用传感器DS18B20模块进行温度测定，（可以自选其他传感器模块）
 - 利用nodemcu连接wifi，并作为服务器使用，服务器更新温度数据至网页。作为服务器使用时，nodemcu会提供一个ip，在电脑端局域网访问此ip，获得温度数据数据
 - 利用Python自动获取温度数据，并利用matplotlib模块进行动态图处理，实现实时+作图检测

## 连接
![](http://i.imgur.com/lpoKg34.jpg)
温度模块的VCC端接在nodemcu的3V3上，总线端接到pin9（即D9）上，有些板子是接在RX上（可以自行设置）

## 代码
- 将init.lua代码烧写到nodemcu中，由于init.lua是开机即执行，因而在测试时，**推荐在最后一行加上file.remove("init.lua")，避免发生每次开机遇到问题重复执行init.lua陷入死循环的情况**
- **init.lua**中：
 - 首先设置了wifi.station模式，作为“服务器”，需要提供wifi ssid和key，一旦连接上，打印IP地址，之后就可以让其他处于同一局域网的设备访问
 - 之后进行一些协议相关的设置，并处理温度数据
 - 用`client:send()`对服务器发送内容，将直接显示在网页上，可使用html语言

- **get_data.py中**：
 - 首先用urllib获取nodemcu创建的网页的内容，运行时在我的电脑上报了错，但错误内容正好就是温度数据，所以获取错误信息作为得到的数据
 - 之后利用matplotlib创建一个动态可视化的图，需要建立一个以yield返回的函数，之后animation.FuncAnimation内需要yield的数值进行更新
 
- 网页效果：
![](http://i.imgur.com/1X2aLBZ.png)
- 最终的动态效果（这里采用4张静态图代替动态图）
![](http://i.imgur.com/q46b6N5.jpg)