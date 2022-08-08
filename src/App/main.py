import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'hal'))
import intruder_detected
import keypad
import RFID
import time
from threading import Thread
import hal_led as led
import hal_lcd as LCD
import hal_servo as servo
import hal_usonic as detect
import hal_buzzer as alarm
import hal_input_switch as lock
import raspberry_pi_webserver as web


def main():
    #initialization of HAL modules
    global Run_Multithread

    Run_Multithread = True

    lock.init()
    detect.init()
    alarm.init()
    led.init()
    lcd = LCD.lcd()
    servo.init()
    lcd.lcd_clear()
    #lcd.lcd_display_string("Template", 2)
    intruder_detected.alarmstart()
    keypad.test()
    RFID.main()
    #web.webserver()


if __name__ == '__main__':
    main()