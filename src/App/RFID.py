import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'hal'))
import time
import hal_lcd as LCD
import hal_servo as servo
from threading import Thread
import hal_rfid_reader as rfid_reader
import hal_input_switch as lock
def main():
    lcd = LCD.lcd()
    reader = rfid_reader.init()
    servo.init()
    lock.init()


    while True:
        id = reader.read_id_no_block()
        id = str(id)

        print("RFID card ID = " + id)



        if id == '854655479803' and lock.read_slide_switch()==1:   #RFID key id
            lcd.lcd_clear()
            lcd.lcd_display_string("Acess granted  ",1)
            time.sleep(2)
            lcd.lcd_clear()
            servo.set_servo_position(90)



        if id!="None" and id!= "854655479803" and lock.read_slide_switch()==1:
            lcd.lcd_clear()
            lcd.lcd_display_string("Access denied",1)
            lcd.lcd_clear()
            servo.set_servo_position(0)




def test():

    RFID_thread = Thread(target=main)
    RFID_thread.start()
if __name__ == '__main__':
    main()