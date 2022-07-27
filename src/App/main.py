import time

from hal import hal_led as led
from hal import hal_lcd as LCD
from hal import hal_rfid_reader as rfid_reader
from hal import hal_keypad as keypad
from threading import Thread
def key_pressed(key):
    password=[]
    password.append(key)

    print(password)


def keypad_thread():

    for i in range(6) :
        key=[]
        key=keypad.get_key()
        i+=i+1
    print(key)




def main():
    #initialization of HAL modules
    led.init()

    lcd = LCD.lcd()

    lcd.lcd_clear()

    lcd.lcd_display_string("Mini-Project", 1)
    lcd.lcd_display_string("Template", 2)
    lcd.lcd_clear()


    keypad.init(key_pressed)

# Start the keypad scanning which will run forever in an infinite while(True) loop in a new Thread "keypad_thread"
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()
    reader = rfid_reader.init()

    while True:
        id = reader.read_id_no_block()
        id = str(id)

        print("RFID card ID = " + id)
        if id=="None":
            lcd.lcd_display_string("Press KeyCard")

        elif id == '988654710544':

            led.set_output(1, 0)
            lcd.lcd_display_string("Door unlocked")

        else:
            lcd.lcd_clear()
            lcd.lcd_display_string("Door locked")
            break
if __name__ == '__main__':
    main()