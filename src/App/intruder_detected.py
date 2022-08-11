import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'hal'))
import hal_buzzer as alarm
import hal_input_switch as lock
import hal_usonic as detect
from threading import Thread
import time
def alarmsound():
    #print(detect.get_distance())
    #print(lock.read_slide_switch())
    #1 is lock 0 is unlock
    while(True):
        if(lock.read_slide_switch()==1):
        #if id!=None or id!='1052230762465':
            if(detect.get_distance()<10):
                print("intruder detected")
                #alarm.short_beep(1)

def alarmstart():

    threadintrusion = Thread(target=alarmsound)
    threadintrusion.start()