import time

from hal import hal_led as led
from hal import hal_lcd as LCD





def main():
    #initialization of HAL modules
    led.init()
    lcd = LCD.lcd()

    lcd.lcd_clear()

    lcd.lcd_display_string("Mini-Project", 1)
    lcd.lcd_display_string("Template", 2)

    while(True):
        led.set_output(1, 1)
        time.sleep(1)

        led.set_output(1, 0)
        time.sleep(1)


if __name__ == '__main__':
    main()