import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'hal'))
import time
import hal_led as led
import hal_lcd as LCD
import hal_servo as servo
from threading import Thread
import hal_rfid_reader as rfid_reader
import hal_input_switch as lock
def main():
    lcd = LCD.lcd()
    reader = rfid_reader.init()
    servo.init()
    lcd.lcd_display_string("Press keycard", 1)
    lcd.lcd_display_string("or password: ", 2)

    while True:
        id = reader.read_id_no_block()
        id = str(id)

        print("RFID card ID = " + id)
        if id == "None":
            print("nothing")

        if id == '1052230762465':#RFID key id
            lcd.lcd_clear()
            lcd.lcd_display_string("Door unlocked")
            servo.set_servo_position(0)

        if lock.read_slide_switch() == 1 and id == "None":
            lcd.lcd_clear()
            lcd.lcd_display_string("Door locked")
            servo.set_servo_position(90)
            time.sleep(2)





if __name__ == '__main__':
    main()