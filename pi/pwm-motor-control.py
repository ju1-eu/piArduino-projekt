import time    
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)  # Positionsnummern: Pins 1-40
GPIO.setwarnings(False)

controlPin = 35     # (1)

GPIO.setup(controlPin, GPIO.OUT)
pwm = GPIO.PWM(controlPin, 500)  # (2)
pwm.start(0)                      # (3)

try:         
  while True:                         # (4)
    duty = int(input('Enter Tastgrad (0 to 100): '))
    if duty < 0 or duty > 100:
      print('0 to 100')
    else:
      pwm.ChangeDutyCycle(duty)
        
finally:  
  print("Cleaning up")
  GPIO.cleanup()