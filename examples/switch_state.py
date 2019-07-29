#!/usr/bin/env python

import time
import ht0740

print("""switch_state.py - Switches the switch and LED using the state method.

Press Ctrl+C to exit.
""")

switch = ht0740.Switch()
print("Enabling switch!")
switch.enable()
state = 1

try:
    while True:
        print("Switch state: {}".format(state))
        switch.switch.set(state)
        switch.led.set(state)
        time.sleep(1)
        state = 1 - state

except KeyboardInterrupt:
    print("Disabling switch")
    switch.disable()
