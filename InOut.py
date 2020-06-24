import setup

from gpiozero import LED, Button, Servo

servo = Servo(setup.LOCK_SERVO_PIN)

cam_unlock = Button(setup.BUTTON_CAM_PIN)
cam_lock = Button(setup.BUTTON_LOCK_PIN)
lock = Button(setup.BUTTON_LOCK_REAR_PIN)
unlock = Button(setup.BUTTON_UNLOCK_REAR_PIN)

led_red = LED(setup.LOCK_LEDRED_PIN)
led_grn = LED(setup.LOCK_LEDGRN_PIN)