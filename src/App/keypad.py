import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'hal'))

import hal_keypad as keypad
import hal_servo as servo
import hal_lcd as LCD
from threading import Thread

import time

password=[]
password1 = [1,2,3,4]
password2 = [2,3,4,5]
password3 = [3,4,5,6]
password4 = [4,5,6,7]
def key_pressed(key):
    lcd = LCD.lcd()
    password.append(key)
    print(password)

    if len(password) != len(password1):
        lcd.lcd_display_string("Press password:", 1)

    if len(password) == 1:
        lcd.lcd_display_string("*", 2)
    if len(password) == 2:
        lcd.lcd_display_string("**", 2)
    if len(password) == 3:
        lcd.lcd_display_string("***", 2)


    if len(password) == len(password1):
        if password == password1:
            lcd.lcd_clear()
            print("Access granted")
            lcd.lcd_display_string("Access granted  ")
            servo.set_servo_position(90)
            return True
        elif password == password2:
            print("Access granted  ")
            servo.set_servo_position(90)
        elif password == password3:
            print("Access granted  ")
            servo.set_servo_position(90)
        elif password == password4:
            print("Access granted  ")
            servo.set_servo_position(90)
        else:
            lcd.lcd_display_string("Access denied  ")
        password.clear()

def test():

    keypad.init(key_pressed)
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()

