from statistics import mean
from colorzero import Color
from gpiozero import SPIDevice, SourceMixin
#from gpiozero.pins.pigpio import PiGPIOFactory

max_brightness = 31

class Pixel:
    def __init__(self, parent, index, brightness=0.5):
        self.parent = parent
        self.index = index
        self._color = (1, 1, 1)
        self._brightness_int = int(brightness * max_brightness)

    @property
    def color(self):
        return Color(*self._color)

    @color.setter
    def color(self, c):
        r, g, b = c
        self._color = (r, g, b)
        self.parent.apply(False)

    @property
    def value(self):
        return self._color

    @value.setter
    def value(self, value):
        self.color = value

    @property
    def r(self):
        return self._color[0]

    @property
    def g(self):
        return self._color[1]

    @property
    def b(self):
        return self._color[2]

    @property
    def brightness(self):
        return self._brightness_int / max_brightness

    @brightness.setter
    def brightness(self, b):
        self.brightness_int = int(b * max_brightness)

    @property
    def brightness_int(self):
        return self._brightness_int

    @brightness_int.setter
    def brightness_int(self, b):
        self._brightness_int = b
        if self._brightness_int < 0:
            self._brightness_int = 0
        if self._brightness_int > max_brightness:
            self._brightness_int = max_brightness
        self.parent.apply(False)

    def on(self):
        self.color = (1, 1, 1)

    def off(self):
        self.color = (0, 0, 0)

class RGBXmasTree(SourceMixin, SPIDevice):
    def __init__(self, pixels=25, brightness=0.5, mosi_pin=12, clock_pin=25, *args, **kwargs):
        super(RGBXmasTree, self).__init__(mosi_pin=mosi_pin,
                                          clock_pin=clock_pin,
                                          *args,
                                          **kwargs)
        #self._spi.rate = 250000
        self._all = [Pixel(parent=self, index=i, brightness=brightness) for i in range(pixels)]
        self.updates_enabled = True
        self.on()

    def __len__(self):
        return len(self._all)

    def __getitem__(self, index):
        return self._all[index]

    def __iter__(self):
        return iter(self._all)

    @property
    def value(self):
        return [p.value for p in self]

    @value.setter
    def value(self, value):
        was_enabled = self.updates_enabled
        self.updates_enabled = False
        for i in range(0, len(value)):
            self[i].value = value[i]
        self.updates_enabled = was_enabled
        self.apply(False)

    @property
    def color(self):
        average_r = mean(pixel.color[0] for pixel in self)
        average_g = mean(pixel.color[1] for pixel in self)
        average_b = mean(pixel.color[2] for pixel in self)
        return Color(average_r, average_g, average_b)

    @color.setter
    def color(self, c):
        was_enabled = self.updates_enabled
        self.updates_enabled = False
        for p in self:
            p.color = c
        self.updates_enabled = was_enabled
        self.apply(False)

    @property
    def brightness(self):
        return self.brightness_int / max_brightness

    @brightness.setter
    def brightness(self, brightness):
        self.brightness_int = int(brightness * max_brightness)

    @property
    def brightness_int(self):
        return int(mean(p.brightness_int for p in self))

    @brightness_int.setter
    def brightness_int(self, b):
        was_enabled = self.updates_enabled
        self.updates_enabled = False
        for p in self:
            p.brightness_int = b
        self.updates_enabled = was_enabled
        self.apply(False)

    def apply(self, force=True):
        if not (self.updates_enabled or force):
            return

        start_of_frame = [0] * 4
        end_of_frame = [0] * 5
        pixels = [[0b11100000 | p.brightness_int, int(p.b * 255), int(p.g * 255), int(p.r * 255)] for p in self]
        pixel_bytes = [i for p in pixels for i in p]
        data = start_of_frame + pixel_bytes + end_of_frame
        self._spi.transfer(data)

    def on(self):
        self.color = (1, 1, 1)

    def off(self):
        self.color = (0, 0, 0)

    def close(self):
        super(RGBXmasTree, self).close()

if __name__ == '__main__':
    tree = RGBXmasTree()
    tree.on()
    # try:
    #     tree.on()
    # finally:
    #     tree.close()
