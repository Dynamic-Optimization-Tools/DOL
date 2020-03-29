class interval(object):
    i_lb = (None, None)    # Left border of the interval: (x, y)
    i_rb = (None, None)    # Right border of the interval: (x, y)
    i_R = None           # Interval characteristic

    def __init__(self):
        pass

    def __SetILb(self, _i_lb):
        self.i_lb = _i_lb

    def __SetIRb(self, _i_rb):
        self.i_rb = _i_rb

    def __SetIR(self, _i_R):
        self.i_R = _i_R

    def GetPiyavskyCharacteristic(self, _lip):
        return 0.5 * _lip * (self.i_rb[0] - self.i_lb[0]) \
            - 0.5 * (self.i_rb[1] - self.i_lb[1])

    def GetStronginCharacteristic(self, _lip):
        return _lip * (self.i_rb[0] - self.i_lb[0]) + \
            ((self.i_rb[1] - self.i_lb[1])**2) / (_lip * \
            (self.i_rb[0] - self.i_lb[0])) -2 * (self.i_rb[1] - self.i_lb[1])

    