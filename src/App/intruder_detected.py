sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'hal'))

import time
from threading import Thread
import hal_lcd as LCD
import hal_usonic as detect
import hal_buzzer as alarm
import hal_input_switch as lock

