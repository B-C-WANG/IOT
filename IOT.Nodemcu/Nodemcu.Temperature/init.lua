print('Setting up WIFI...') 
wifi.setmode(wifi.STATION)
wifi.sta.config('替换成自己的wifi名称', 'wifi密码')
wifi.sta.connect()
tmr.alarm(1, 1000, tmr.ALARM_AUTO, function()
    if wifi.sta.getip() == nil then
        print('Waiting for IP ...')
    else
        print('IP is ' .. wifi.sta.getip())--这里要记住ip，后面会用到
    tmr.stop(1)
    end
end)
srv=net.createServer(net.TCP)  
srv:listen(80,function(conn)  
    conn:on("receive", function(client,request)  
        local buf = "";  
        local _, _, method, path, vars = string.find(request, "([A-Z]+) (.+)?(.+) HTTP");  
        if(method == nil)then  
            _, _, method, path = string.find(request, "([A-Z]+) (.+) HTTP");  
        end  
        local _GET = {}  
        if (vars ~= nil)then  
            for k, v in string.gmatch(vars, "(%w+)=(%w+)&*") do  
                _GET[k] = v  
            end  
        end  
        pin = 9
ow.setup(pin)
count = 0
repeat
  count = count + 1
  addr = ow.reset_search(pin)
  addr = ow.search(pin)
  tmr.wdclr()
until((addr ~= nil) or (count > 100))
if (addr == nil) then
  print("No more addresses.")
else
  --print(addr:byte(1,8))
  crc = ow.crc8(string.sub(addr,1,7))
  if (crc == addr:byte(8)) then
    if ((addr:byte(1) == 0x10) or (addr:byte(1) == 0x28)) then
      --print("Device is a DS18S20 family device.")
          ow.reset(pin)
          ow.select(pin, addr)
          ow.write(pin, 0x44, 1)
          tmr.delay(1000000)
          present = ow.reset(pin)
          ow.select(pin, addr)
          ow.write(pin,0xBE,1)  
          data = nil
          data = string.char(ow.read(pin))
          for i = 1, 8 do
            data = data .. string.char(ow.read(pin))
          end
          crc = ow.crc8(string.sub(data,1,8))
          if (crc == data:byte(9)) then
             t = (data:byte(1) + data:byte(2) * 256)
             if (t > 0x7fff) then
                t = t - 0x10000
             end
             if (addr:byte(1) == 0x28) then
                t = t * 625
             else
                t = t * 5000
             end
             local sign = ""
             if (t < 0) then
                 sign = "-"
                 t = -1 * t
             end
             local t1 = string.format("%d", t / 10000)
             local t2 = string.format("%04u", t % 10000)
             temp = sign .. t1 .. "." .. t2
             --print("Temperature= " .. temp .. " Celsius")
          end                   
          tmr.wdclr() 
    else
      print("Device family is not recognized.")
    end
  else
    print("CRC is not valid!")
  end
end
buf="" 
        buf = buf..temp
        client:send(buf);    
        client:close();  
        collectgarbage();  
    end)  
end)
--file.remove("init.lua")