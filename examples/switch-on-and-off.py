#!/usr/bin/env python

import time
import ht0740

print("""switch-on-and-off.py - Enables switch then turns it on and off
Press Ctrl+C to exit.
""")

switch = ht0740.Switch()

print("Enabling switch...")
switch.enable()
time.sleep(1)

print("Turning switch and LED on...")
switch.on()
time.sleep(1)

print("Turning switch and LED off...")
switch.off()
time.sleep(1)

print("Turning only the LED on...")
switch.led.on()
time.sleep(1)

print("Turning only the LED off...")
switch.led.off()
time.sleep(1)

print("Turning only the switch on...")
switch.switch.on()
time.sleep(1)

print("Turning only the switch off...")
switch.switch.off()

print("Disabling switch...")
switch.disable()
time.sleep(1)
