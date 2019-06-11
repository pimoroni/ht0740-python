from i2cdevice import Device, Register, BitField

__version__ = '0.0.1'


class IO_ITEM:
    def __init__(self, i2c_object, pin_io, inverted=False):
        self.enabled = True
        self.status = False
        self.i2c_object = i2c_object
        self.pin_io = pin_io
        self.inverted = inverted

    def state(self):

        return self.i2c_object.OUTPUT.get_value()

    def on(self):
        if self.enabled:

            if self.inverted:
                self.i2c_object.OUTPUT.set_value(self.state() & ~(1 << self.pin_io))
                print('on', self.state() & ~(1 << self.pin_io))

            else:
                self.i2c_object.OUTPUT.set_value(self.state() | (1 << self.pin_io))

    def off(self):
        if self.enabled:
            if self.inverted:
                self.i2c_object.OUTPUT.set_value(self.state() | (1 << self.pin_io))

            else:
                self.i2c_object.OUTPUT.set_value(self.state() & ~(1 << self.pin_io))

    def disable(self):
        self.i2c_object.CONFIG.set_value(self.i2c_object.CONFIG.get_value() | 1 << self.pin_io)
        self.enabled = False

    def enable(self):
        self.i2c_object.CONFIG.set_value(self.i2c_object.CONFIG.get_value() & ~(1 << self.pin_io))
        self.enabled = True


class PCA9554A:
    def __init__(self, i2c_addr=0x38, i2c_dev=None):
        self._i2c_addr = i2c_addr
        self._i2c_dev = i2c_dev
        self._is_setup = False
        # Device definition
        self._pca9554a = Device(self._i2c_addr, i2c_dev=self._i2c_dev, bit_width=8, registers=(
            Register('INPUT', 0x00, fields=(
                BitField('value', 0xFF),
                BitField('switch', 0b00001000),
                BitField('led', 0b00000001)
            )),
            Register('OUTPUT', 0x01, fields=(
                BitField('value', 0xFF),
                BitField('switch', 0b00001000),
                BitField('led', 0b00000001)
            )),
            Register('INVERT', 0x02, fields=(
                BitField('value', 0xFF),
                BitField('switch', 0b00001000),
                BitField('led', 0b00000001)
            )),
            Register('CONFIG', 0x03, fields=(
                BitField('value', 0xFF),
                BitField('switch', 0b00001000),
                BitField('led', 0b00000001)
            )),
        ))
        #  Set IO configureation for driving Switch and LED
        self._pca9554a.OUTPUT.set_switch(0)
        self._pca9554a.OUTPUT.set_led(1)
        self._pca9554a.CONFIG.set_switch(0)
        self._pca9554a.CONFIG.set_led(0)
        self.led_enable = True
        self.switch_enabled = True
        self.led_status = False
        self.switch_status = False


class SWITCH:

    def __init__(self, i2c_addr=0x38, i2c_dev=None):
        self._i2c_addr = i2c_addr
        self._i2c_dev = i2c_dev
        self._is_setup = False
        self.led_io = 0

        self.switch_io = 3

        self.io_controller = PCA9554A(self._i2c_addr, self._i2c_dev)
        self.led = IO_ITEM(self.io_controller._pca9554a, self.led_io, inverted=True)
        self.switch = IO_ITEM(self.io_controller._pca9554a, self.switch_io)

    def on(self):
        self.led.on()
        self.switch.on()

    def off(self):
        self.led.off()
        self.switch.off()

    def disable(self):
        self.led.disable()
        self.switch.disable()

    def enable(self):
        self.led.enable()
        self.switch.enable()


if __name__ == "__main__":

    import smbus
    import time
    bus = smbus.SMBus(1)

    switch = SWITCH(i2c_addr=[0x38, 0x39, 0x3A, 0x3B], i2c_dev=bus)

    while 1:

        switch.on()
        time.sleep(0.5)
        switch.off()
        time.sleep(0.5)
