import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
TRIG1 = 23
ECHO1 = 24
TRIG2 = 20
ECHO2= 21
print "HC-SR04 mesafe sensoru"

GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)
GPIO.setup(TRIG2,GPIO.OUT)
GPIO.setup(ECHO2,GPIO.IN)
pulse_start1=0
pulse_end1=0
distance1=0
pulse_duration1=0
pulse_start2=0
pulse_end2=0
distance2=0
pulse_duration2=0
while True:

  GPIO.output(TRIG1, False)
  time.sleep(1)
  GPIO.output(TRIG1, True)
  time.sleep(0.00001)
  GPIO.output(TRIG1, False)
  while GPIO.input(ECHO1)==0:
    pulse_start1 = time.time()
  while GPIO.input(ECHO1)==1:
    pulse_end1 = time.time()
  pulse_duration1 = pulse_end1- pulse_start1
  distance1 = pulse_duration1 * 17150
  distance1 = round(distance1, 2)
  
  GPIO.output(TRIG2, False)
  time.sleep(1)
  GPIO.output(TRIG2, True)
  time.sleep(0.00001)
  GPIO.output(TRIG2, False)
  while GPIO.input(ECHO2)==0:
    pulse_start2 = time.time()
  while GPIO.input(ECHO2)==1:
    pulse_end2 = time.time()
  pulse_duration2 = pulse_end2- pulse_start2
  distance2 = pulse_duration2 * 17150
  distance2 = round(distance2, 2)
  
  print("Sensor 1:",distance1)
  print("Sensor 2:",distance2)

