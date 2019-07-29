#!/usr/bin/env python

import time
import ht0740

print("""toggle_led.py - Toggles LED on and off using the toggle method.

Press Ctrl+C to exit.
""")

switch = ht0740.Switch()
print("Enabling switch!")
switch.enable()

try:
    while True:
        print("LED state: {}".format(switch.led.state()))
        switch.led.toggle()
        time.sleep(1)

except KeyboardInterrupt:
    print("Disabling switch")
    switch.disable()
