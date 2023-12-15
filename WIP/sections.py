from tree import RGBXmasTree, Pixel

botPixels = (0,16,15,6,12,24,19,7);
midPixels = (17,14,5,23,20,8,1,11);
topPixels = (18,13,10,22,21,9,4,2);

class TreeBottom(RGBXmasTree):
    def __init__(self, pixels=8, brightness=0.5, mosi_pin=12, clock_pin=25, *args, **kwargs):
        super().__init__(mosi_pin=mosi_pin, clock_pin=clock_pin, *args, **kwargs)
        self._all = [Pixel(parent=TreeBottom, index=botPixels[i]) for i in range(pixels)]

class TreeMiddle(RGBXmasTree):
    def __init__(self, pixels=8, brightness=0.5, mosi_pin=12, clock_pin=25, *args, **kwargs):
        super().__init__(mosi_pin=mosi_pin, clock_pin=clock_pin, *args, **kwargs)
        self._all = [Pixel(parent=TreeMiddle, index=botPixels[i]) for i in range(pixels)]

class TreeTop(RGBXmasTree):
    def __init__(self, pixels=8, brightness=0.5, mosi_pin=12, clock_pin=25, *args, **kwargs):
        super().__init__(mosi_pin=mosi_pin, clock_pin=clock_pin, *args, **kwargs)
        self._all = [Pixel(parent=TreeTop, index=botPixels[i]) for i in range(pixels)]
