import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'hal'))

import hal_keypad as keypad
import hal_servo as servo
import hal_lcd as LCD
import passcheck as passwordfile
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
        if  passwordfile.test_password1(password) == True:
            lcd.lcd_clear()
            print("Access granted")
            lcd.lcd_display_string("Access granted  ")
            servo.set_servo_position(90)
            password.clear()
        elif passwordfile.test_password2(password) == True:
            print("Access granted  ")
            lcd.lcd_display_string("Access granted  ")
            servo.set_servo_position(90)
            password.clear()
        elif passwordfile.test_password3(password) == True:
            print("Access granted  ")
            lcd.lcd_display_string("Access granted  ")
            servo.set_servo_position(90)
            password.clear()
        elif passwordfile.test_password4(password) == True:
            print("Access granted  ")
            lcd.lcd_display_string("Access granted  ")
            servo.set_servo_position(90)
            password.clear()
        else:
            lcd.lcd_display_string("Access denied  ")
            password.clear()
def pytestkeypad(arr):
    if arr == password1:
        return True
    elif password == password2:
        return True
    elif password == password3:
        return True
    elif password == password4:
        return True
    else:
        return False
def test():

    keypad.init(key_pressed)
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()

