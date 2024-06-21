#######################################################
#    Developer: ConfusedTomatoDev
#    Created 06/03/2024
#
#    updown.py
#    Use this script from root to flap
#    interfaces on a linux host at random intervals
#######################################################

import os
import random
import time
import signal
import sys
from datetime import datetime

# Define interface
interface = "eth1"

# Catch the time
curtime = datetime.now().strftime("%Y-%m-%d " "%H:%M:%S")

def timestamp():
    return datetime.now().strftime("%H:%M:%S")

# Define flap interval and interval to sleap between flaps.
minint = 1
maxint = 15
pauseint = 5

# Prepare for the unexpected
def cleanup(signum, frame):
    print(f"Caught signal {signum}, ifup {interface}")
    os.system(f"ifup {interface}")
    sys.exit(0)

# SIGHUP
signal.signal(signal.SIGHUP, cleanup)
# SIGINT
signal.signal(signal.SIGINT, cleanup)
# SIGTERM
signal.signal(signal.SIGTERM, cleanup)

# Start the flapping
try:
    while True:
        print(f"#### {curtime} ####")
        print(f"{timestamp()} - Interval Start")
        interval = random.randint(minint, maxint)
        print(f"Start selected downtime {interval}")
        os.system(f"ifdown {interface}")
        time.sleep(interval)
        os.system(f"ifup {interface}")
        print(f"{timestamp()} - End selected downtime")
        time.sleep(pauseint)
        print(f"Up after {pauseint}")
        print(f"{timestamp()} Wakeup\n\n")

# Handle the unexpected
except Exception as e:
    print(f"Script ended unexpectedly: {e}")
    os.system(f"ifup {interface}")
    print("Ended Cycle\n")
