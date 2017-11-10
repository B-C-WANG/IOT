import RPi.GPIO as GPIO
import time
#pin: the second to vcc:5v power supply
#pin: the ground to gnd
#GPIO2, the third, to Trig, to make ultrasonic come out
#GPIO3, the fifth, to Echo， to get ultrasonic.
def measure_distance(speed_of_sound):

        #give the signal to come out ultrasonic
        GPIO.output(2,GPIO.HIGH)
        #keep > 10us（there is 15us）
        time.sleep(0.000015)
        GPIO.output(2,GPIO.LOW)
        while not GPIO.input(3):#GPIO.input is a bool result,of 1 or 0
                pass
        #when it is high ,start to time count
        t1 = time.time()
        while GPIO.input(3):
                pass
        #when it is low, stop
        t2 = time.time()
        #return the distance, pay attention to different speed of sound , need to measure
        return (t2-t1)*speed_of_sound/2
GPIO.setmode(GPIO.BCM)
#the third pin is GPIO2
GPIO.setup(2,GPIO.OUT,initial=GPIO.LOW)
#the fifth pin is GPIO3
GPIO.setup(3,GPIO.IN)

time.sleep(2)
try:
        while True:
                print 'Distance: %0.2f m' %measure_distance(340)
                time.sleep(1)
except KeyboardInterrupt:
        GPIO.cleanup()