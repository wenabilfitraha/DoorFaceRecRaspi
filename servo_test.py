from gpiozero import Servo
from time import sleep

servo = Servo(4)
servo.min()
sleep(10)