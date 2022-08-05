import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'hal'))
import time
import hal_led as led
import hal_lcd as LCD
import hal_servo as servo
from threading import Thread
import hal_rfid_reader as rfid_reader
def main():
    lcd = LCD.lcd()
    reader = rfid_reader.init()
    servo.init()


    while True:
        id = reader.read_id_no_block()
        id = str(id)

        print("RFID card ID = " + id)
        if id == "None":
            lcd.lcd_display_string("Press KeyCard")

        elif id == '988654710544':
            servo.set_servo_position(90)
            led.set_output(1, 0)
            lcd.lcd_display_string("Door unlocked")

        else:
            lcd.lcd_clear()
            lcd.lcd_display_string("Door locked")
            servo.set_servo_position(0)
            time.sleep(2)



if __name__ == '__main__':
    main()