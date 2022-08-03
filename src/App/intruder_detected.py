import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'hal'))

import hal_buzzer as alarm
import hal_input_switch as lock
import hal_usonic as detect
from threading import Thread
import time
def alarmsound():

    while(True):
        #print(detect.get_distance())
        #print(lock.read_slide_switch())
        #switch to the right is 0 to the left is 1
        #1 is lock 0 is unlock
        if(detect.get_distance()>10):
            if(lock.read_slide_switch()==1):
                print("intruder detected")
                #alarm.short_beep(1)

def alarmstart():
    global Run_Multithread

    Run_Multithread = True
    threadintrusion = Thread(target=alarmsound)
    threadintrusion.start()