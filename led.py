import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

pwm_led=GPIO.PWM(18,500)
pwm_led.start(100)
while (True):
  duty=int(input())
  pwm_led.ChangeDutyCycle(duty)

import RPi.GPIO as GPIO
import time

# Define GPIO pins for stepper motor
step_pin = 17  # Change this to the GPIO pin you have connected to the STEP input on your stepper motor driver
dir_pin = 27   # Change this to the GPIO pin you have connected to the DIR input on your stepper motor driver

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(step_pin, GPIO.OUT)
GPIO.setup(dir_pin, GPIO.OUT)

# Function to move the stepper motor
def move_stepper(steps, delay=0.01):
    # Set direction (1 for clockwise, 0 for counterclockwise)
    GPIO.output(dir_pin, 1)  # Change this value if you want to change the direction

    # Move the stepper motor
    for _ in range(steps):
        GPIO.output(step_pin, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(step_pin, GPIO.LOW)
        time.sleep(delay)

# Move the stepper motor 200 steps (adjust as needed)
move_stepper(200)

# Cleanup GPIO
GPIO.cleanup()
