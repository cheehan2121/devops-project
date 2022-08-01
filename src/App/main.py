import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'hal'))
import intruder_detected
import keypad
import time
from threading import Thread
import hal_led as led
import hal_lcd as LCD
import hal_servo as servo
import hal_usonic as detect
import hal_buzzer as alarm
import hal_input_switch as lock

def alarmsound():
    while(1==1):
        print(detect.get_distance())
        print(lock.read_slide_switch())
        #switch to the right is 0 to the left is 1
        #1 is lock 0 is unlock
        if(detect.get_distance()>10):
            if(lock.read_slide_switch()==1):
             print("intruder detected")
             alarm.short_beep(1)

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
    lcd.lcd_display_string("Mini-Project", 1)
    lcd.lcd_display_string("Template", 2)
    #threadintrusion =Thread(target=alarmsound())
    #threadintrusion.start()
    #intruder_detected.alarmstart()
    keypad.test()

if __name__ == '__main__':
    main()