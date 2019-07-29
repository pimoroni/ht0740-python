#!/usr/bin/env python

import time
import ht0740

print("""toggle_all.py - Toggles the switch and LED on and off continuously.

Press Ctrl+C to exit.
""")

switch = ht0740.Switch()
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
