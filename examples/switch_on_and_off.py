#!/usr/bin/env python

import time
from ht0740 import HT0740

print("""switch_on_and_off.py - Switches the switch and LED using the on and off methods.

Press Ctrl+C to exit.
""")

switch = HT0740()
print("Enabling switch!")
switch.enable()
state = 1

try:
    while True:
        print("Switching switch and LED on!")
        switch.switch.on()
        switch.led.on()
        time.sleep(1)
        print("Switching switch and LED off!")
        switch.switch.off()
        switch.led.off()
        time.sleep(1)

except KeyboardInterrupt:
    print("Disabling switch")
    switch.disable()
