import sys
from i2cdevice import MockSMBus
import mock


def test_setup():
    sys.modules['smbus'] = mock.Mock()
    sys.modules['smbus'].SMBus = MockSMBus
    import ht0740
    switch = ht0740.Switch()
    switch.on()
    switch.off()
    switch.led.disable()
    switch.switch.disable()
    switch.disable()
    switch.on()
    switch.off()
    switch.led.enable()
    switch.switch.enable()
    switch.enable()
    switch.on()
    switch.off()



