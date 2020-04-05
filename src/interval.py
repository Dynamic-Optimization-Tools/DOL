import sys
import math

class interval(object):
    _i_lb = (None, None)    # Left border of the interval: (x, y)
    _i_rb = (None, None)    # Right border of the interval: (x, y)
    _i_R = None             # Interval characteristic

    def __init__(self, i_lb, i_rb):
        self.__InitializeData(i_lb, i_rb)

    def GetILb(self):
        return self._i_lb

    def GetIRb(self):
        return self._i_rb

    def GetIR(self):
        return self._i_R

    def __InitializeData(self, _i_lb, _i_rb):
        self.__SetILb(_i_lb)
        self.__SetIRb(_i_rb)

    def __SetILb(self, _i_lb):
        self._i_lb = _i_lb

    def __SetIRb(self, _i_rb): 
        self._i_rb = _i_rb

    def __SetIR(self, _i_R):
        self._i_R = _i_R

    def GetPiyavskyCharacteristic(self, _lip):
        try:
            self._i_R = 0.5 * _lip * (self._i_rb[0] - self._i_lb[0])  - 0.5 * (self._i_rb[1] + self._i_lb[1])
            return 0
        except TypeError:
            print("Incorrect type of variable in \'GetPiyavskyCharacteristic\' function")
            sys.exit(1)

    def GetStronginCharacteristic(self, _lip):
        try:
            self._i_R = _lip * (self._i_rb[0] - self._i_lb[0]) + \
                math.pow((self._i_rb[1] - self._i_lb[1]), 2) / (_lip * \
                (self._i_rb[0] - self._i_lb[0])) - 2 * (self._i_rb[1] + self._i_lb[1])
        except TypeError:
            print("ERROR: Incorrect type of variable in \'GetStronginCharacteristic\' function.")
            sys.exit(1)
        except ZeroDivisionError:
            print("ERROR: Zero division in \'GetStronginCharacteristic\' function.")
            sys.exit(2)

    def GetBruteForceCharacteristic(self, _lip):
        try:
            self._i_R = self.GetIRb()[0] - self.GetILb()[0]
        except TypeError:
            print("ERROR: Incorrect type of variable in \'GetBruteForceCharacteristic\' function.")
            sys.exit(1)

