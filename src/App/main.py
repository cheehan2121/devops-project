import time

from hal import hal_led as led
from hal import hal_lcd as LCD
from hal import hal_servo as servo
from hal import hal_usonic as detect
from hal import hal_buzzer as alarm


def main():
    #initialization of HAL modules
    intruder_detected=0
    detect.init()
    alarm.init()
    led.init()
    lcd = LCD.lcd()
    servo.init()
    lcd.lcd_clear()


    while True:
        print(detect.get_distance())
        if(detect.get_distance()<5):
            print("intruder detected")
            intruder_detected=1
            break


    lcd.lcd_display_string("Mini-Project", 1)
    lcd.lcd_display_string("Templatb", 2)


    while(intruder_detected==1):
        alarm.short_beep(0.5)

if __name__ == '__main__':
    main()