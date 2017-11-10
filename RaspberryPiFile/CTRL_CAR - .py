

import RPi.GPIO as io
import time
io.setmode(io.BOARD)
io.cleanup()

left_motor_go=13# see where arduino's 8 is then,raspberry connect it , output type keep the same
#8 will change according to raspberry's gpio
left_motor_back=15
right_motor_go=16
right_motor_back=18

io.setup(left_motor_go,io.OUT)
io.setup(left_motor_back,io.OUT)
io.setup(right_motor_back,io.OUT)
io.setup(right_motor_go,io.OUT)

def forward():
    io.output(left_motor_go,0)
    io.output(left_motor_back,1)

    io.output(right_motor_go,1)#pay attention, it is different!
    io.output(right_motor_back,0)

def stop():
    io.output(left_motor_go, 0)
    io.output(left_motor_back, 0)

    io.output(right_motor_go, 0)  # pay attention, it is different!
    io.output(right_motor_back, 0)

def left():
    io.output(left_motor_go, 0)
    io.output(left_motor_back, 0)

    io.output(right_motor_go, 1)  # pay attention, it is different!
    io.output(right_motor_back, 0)

def spin_left():
    io.output(left_motor_go, 1)
    io.output(left_motor_back, 0)

    io.output(right_motor_go, 1)  # pay attention, it is different!
    io.output(right_motor_back, 0)

def right():
    io.output(left_motor_go, 0)
    io.output(left_motor_back, 1)

    io.output(right_motor_go, 0)  # pay attention, it is different!
    io.output(right_motor_back, 0)

def spin_right():
    io.output(left_motor_go, 0)
    io.output(left_motor_back, 1)

    io.output(right_motor_go, 0)  # pay attention, it is different!
    io.output(right_motor_back, 1)

def back():
    io.output(left_motor_go, 1)
    io.output(left_motor_back, 0)

    io.output(right_motor_go, 0)  # pay attention, it is different!
    io.output(right_motor_back, 1)

while 1:
    temp=str(raw_input('go,lf,rt,st,bk, + number of 0.1s'))+'n'
    a=temp[0:2]
    try:
        b=int(temp[2:-1])
    except:
        pass
    if a=='go':
        forward()
        time.sleep(b/10)
        stop()
    elif a=='lf':
        left()
        time.sleep(b/10)
        stop()
    elif a=='rt':
        right()
        time.sleep(b/10)
        stop()

    elif a=='st':
        stop()

    elif a=='bk':
        back()
        time.sleep(b/10)
        stop()
    else:
        pass


