#!/usr/bin/env python

import time
from ht0740 import HT0740

print("""toggle_led.py - Toggles LED on and off using the toggle method.

Press Ctrl+C to exit.
""")

switch = HT0740()
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
