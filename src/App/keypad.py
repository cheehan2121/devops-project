import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'hal'))

import hal_keypad as keypad
import hal_servo as servo
from threading import Thread
import time

password=[]
password1 = [1,2,3,4]
password2 = [2,3,4,5]
password3 = [3,4,5,6]
password4 = [4,5,6,7]
def key_pressed(key):

    password.append(key)
    print(password)
    if len(password) == len(password1):
        if password == password1:
            print("Access granted")
            servo.set_servo_position(90)
        if password == password2:
            print("Access granted")
            servo.set_servo_position(90)
        if password == password3:
            print("Access granted")
            servo.set_servo_position(90)
        if password == password4:
            print("Access granted")
            servo.set_servo_position(90)
        password.clear()
    time.sleep(0.2)

def test():
    keypad.init(key_pressed)
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()

