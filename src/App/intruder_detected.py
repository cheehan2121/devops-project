import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'hal'))
import hal_rfid_reader as rfid_reader
import hal_buzzer as alarm
import hal_input_switch as lock
import hal_usonic as detect
from threading import Thread
import time
def alarmsound():
    reader = rfid_reader.init()
    while(True):
        #print(detect.get_distance())
        #print(lock.read_slide_switch())
        #switch to the right is 0 to the left is 1
        #1 is lock 0 is unlock
        id = reader.read_id_no_block()
        id = str(id)

        if(lock.read_slide_switch()==1):
            #if id!=None or id!='1052230762465':
            if(detect.get_distance()>10):
                if id != "None" and id != "102230762465":
                    print("intruder detected")
                    alarm.short_beep(1)

def alarmstart():
    global Run_Multithread

    Run_Multithread = True
    threadintrusion = Thread(target=alarmsound)
    threadintrusion.start()