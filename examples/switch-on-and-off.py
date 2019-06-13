import ht0740
import time 

print("""switch-on-and-off.py - Enables switch then turns it on and off
Press Ctrl+C to exit.
""")

switch = ht0740.Switch()
print("Enabling switch...")
switch.enable()
time.sleep(1)
print("Turing switch and led on...")
switch.on()
time.sleep(1)
print("Turing switch and led off...")
switch.off()
time.sleep(1)
print("Turing only the led on...")
switch.led.on()
time.sleep(1)
print("Turing only the led off...")
switch.led.off()
time.sleep(1)
print("Turing only the switch on...")
switch.switch.on()
time.sleep(1)
print("Turing only the switch off...")
switch.switch.off()

