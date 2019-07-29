from i2cdevice import Device, Register, BitField

__version__ = '0.0.1'


class IOItem:

    def __init__(self, i2c_object, pin_io, inverted=False):
        self.enabled = True
        self.status = False
        self.i2c_object = i2c_object
        self.pin_io = pin_io
        self.inverted = inverted

    def state(self):
        if self.inverted:
            return ~self.i2c_object.OUTPUT.get_value() >> self.pin_io & 1
        else:
            return self.i2c_object.OUTPUT.get_value() >> self.pin_io & 1

    def set(self, state):
        if self.enabled:
            if self.inverted:
                state = 1 - state
            value = self.i2c_object.OUTPUT.get_value()
            mask = 1 << self.pin_io
            self.i2c_object.OUTPUT.set_value(((value & ~mask) | ((state << self.pin_io) & mask)))

    def on(self):
        self.set(1)

    def off(self):
        self.set(0)

    def toggle(self):
        if self.enabled:
            self.i2c_object.OUTPUT.set_value(self.i2c_object.OUTPUT.get_value() ^ (1 << self.pin_io))

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
        #  Set IO configuration for driving switch and LED
        self._pca9554a.OUTPUT.set_switch(0)
        self._pca9554a.OUTPUT.set_led(1)
        self._pca9554a.CONFIG.set_switch(0)
        self._pca9554a.CONFIG.set_led(0)
        self.led_enable = True
        self.switch_enabled = True
        self.led_status = False
        self.switch_status = False


class HT0740:

    def __init__(self, i2c_addr=0x38, i2c_dev=None):
        self._i2c_addr = i2c_addr
        self._i2c_dev = i2c_dev
        self._is_setup = False
        self.led_io = 0

        self.switch_io = 3

        self.io_controller = PCA9554A(self._i2c_addr, self._i2c_dev)
        self.led = IOItem(self.io_controller._pca9554a, self.led_io, inverted=True)
        self.switch = IOItem(self.io_controller._pca9554a, self.switch_io)

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

    def toggle(self):
        self.led.toggle()
        self.switch.toggle()
