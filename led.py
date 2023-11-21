import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

pwm_led=GPIO.PWM(18,500)
pwm_led.start(100)
while (True):
  duty=int(input())
  pwm_led.ChangeDutyCycle(duty)
