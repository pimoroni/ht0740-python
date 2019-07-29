#!/usr/bin/env python

import time
from ht0740 import HT0740

print("""toggle_all.py - Toggles the switch and LED on and off continuously.

Press Ctrl+C to exit.
""")

switch = HT0740()
print("Enabling switch!")
switch.enable()

try:
    while True:
        switch.toggle()
        print("Switch state: {} LED state: {}".format(switch.switch.state(), switch.led.state()))
        time.sleep(1)

except KeyboardInterrupt:
    print("Disabling switch!")
    switch.disable()
