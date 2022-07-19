import time

from hal import hal_led as led
from hal import hal_lcd as LCD
from hal import hal_rfid_reader as rfid




def main():
    #initialization of HAL modules
    led.init()
    rfid.init()
    lcd = LCD.lcd()
    rfid.init()
    lcd.lcd_clear()

    lcd.lcd_display_string("Mini-Project", 1)
    lcd.lcd_display_string("Template", 2)

    while(True):
        led.set_output(1, 1)
        time.sleep(1)

        led.set_output(1, 0)
        time.sleep(1)

    scan = rfid.SimpleMFRC522
    print(scan)

if __name__ == '__main__':
    main()