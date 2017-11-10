from evdev import InputDevice
from select import select

def detect_input_key():

    dev=InputDevice('/dev/input/event1')#if you don't know what event is your keyboard, open /dev/event and try all
    while 1:
        select([dev],[],[])
        for event in dev.read():
            print 'code:',event.code,'value:',event.value
def detect_input_key2():
    dev=InputDevice('/dev/input/event1')#if you don't know what event is your keyboard, open /dev/event and try all
    while 1:
        select([dev],[],[])
        for event in dev.read():
            if (event.value==1 or event.value==0) and event.code!=0:
                key=event.code
                status=0 if event.value else 1#0 is pressed 1is release

                #you can add a code here to represent a pre-release action
                print key,status
                return key,status
            
                

while 1:
     detect_input_key2()
    
