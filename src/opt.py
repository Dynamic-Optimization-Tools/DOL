import math
import os
import sys
from os.path import dirname as up
root_dir = os.path.join(up(os.path.abspath(os.curdir)))
sys.path.insert(0, root_dir)
from src.interval import interval
from src.solution import solution

class opt(object):
    _lb = None
    _rb = None
    _r = None
    _max_iter = 100
    _minimum = None
    _spent_iter = 0
    _eps = 0.01
    _sol = solution()
    _use_method = None
    _a = None
    _b = None
    _c = None
    _d = None
    
    class methods():
        Piyavsky = "Piyavsky"
        Strongin = "Strongin"
        BruteForse = "BruteForse"

    methods = methods()

    _methods = { 
               "Piyavsky": interval.GetPiyavskyCharacteristic,
               "Strongin": interval.GetStronginCharacteristic,
               "BruteForse": interval.GetBruteForceCharacteristic
               }

    _next_point = {
                  "Piyavsky": lambda _x_l, _x_r, _y_l, _y_r, _lipsh: 0.5 * (_x_r + _x_l) - 0.5 * ((_y_r - _y_l) / _lipsh),
                  "Strongin": lambda _x_l, _x_r, _y_l, _y_r, _lipsh: 0.5 * (_x_r + _x_l) - 0.5 * ((_y_r - _y_l) / _lipsh),
                  "BruteForse": lambda _x_l, _x_r, _y_l, _y_r, _lipsh: _x_l + (_x_r - _x_l) / 2.0
                  }
    
    def __init__(self):
        pass

    def __SetLb(self, _lb):
        self._lb = _lb
    
    def __SetRb(self, _rb):
        self._rb = _rb

    def __SetR(self, _r):
        self._r = _r

    def __SetMethod(self, _method):
        self._use_method = _method

    def __SetSpentIter(self, _spent_iter):
        self._spent_iter = _spent_iter

    def __SetMaxIter(self, _max_iter):
        self._max_iter = _max_iter

    def __SetEps(self, _eps):
        self._eps = _eps

    def __SetMin(self, _min):
        self._minimum = _min
    
    def __PrintError(self, message):
        print('\x1b[1;31m' + 'ERROR: ' + '\x1b[0m' + message)

    def __CorrectnessParameters(self, lb, rb, r, max_iter, method):
        if type(lb) is not float:
            self.__PrintError("Invalid type of parameter \'lb\' (expected \'float\')")
            return False
        elif type(rb) is not float:
            self.__PrintError("Invalid type of parameter \'rb\' (expected \'float\')")
            return False
        elif type(r) is not float:
            self.__PrintError("Invalid type of parameter \'r\' (expected \'float\')")
            return False
        elif type(max_iter) is not int and max_iter is not None:
            self.__PrintError("Invalid type of parameter \'max_iter\' (expected \'float\' or \'None\')")
            return False
        elif method not in self._methods:
            self.__PrintError("Invalid method's name")
            return False
        else:
            return True

    def SetFunctionParameters(self, a, b, c, d):
        if type(a) is not int and type(a) is not float:
            self.__PrintError("Invalid type of parameter \'a\' (expected \'float\' or \'int\')")
        elif type(a) is not int and type(a) is not float:
            self.__PrintError("Invalid type of parameter \'b\' (expected \'float\' or \'int\')")
        elif type(a) is not int and type(a) is not float:
            self.__PrintError("Invalid type of parameter \'c\' (expected \'float\' or \'int\')")
        elif type(a) is not int and type(a) is not float:
            self.__PrintError("Invalid type of parameter \'d\' (expected \'float\' or \'int\')")
        else:
            self._a = a
            self._b = b
            self._c = c
            self._d = d

    def __InitializeData(self, lb, rb, r, max_iter, method, eps):
        self.__SetLb(lb)
        self.__SetRb(rb)
        self.__SetR(r)
        self.__SetMethod(method)
        if max_iter is not None:
            self.__SetMaxIter(max_iter)
        if eps is not None:
            self.__SetEps(eps)

    def Func(self, x):
        return self._a * math.sin(self._b * x) + self._c * math.cos(self._d * x)

    def __UpdateMinValue(self, *args):
        if self._minimum is None:
            self.__SetMin(args[0])
        for arg in args:
            if self._minimum[1] > arg[1]:
                self.__SetMin(arg)

    def __IncreaseIterCount(self):
        self.__SetSpentIter(self._spent_iter + 1)


    def __GetLipsh(self, _intervals):
        M = None
        for i, i_interval in enumerate(_intervals):
            for j_interval in  _intervals[i:]:
                M_interval = abs((j_interval.GetIRb()[1] - i_interval.GetILb()[1]) / (j_interval.GetIRb()[0] - i_interval.GetILb()[0]))
                if M is None:
                    M = M_interval
                else:
                    M = M_interval if M < M_interval else M
        return 1 if M == 0 else self._r * M

    def __GetBestInterval(self, _intervals):
        max_charact = _intervals[0].GetIR()
        num_interval = 0
        for num, interval in enumerate(_intervals):
            if max_charact < interval.GetIR():
                max_charact = interval.GetIR()
                num_interval = num
        return num_interval

    def __GetNewIntervals(self, intervals, lipsh, method):
        num = self.__GetBestInterval(intervals)
        if self.__CheckStop(intervals[num]):
            return 0
        old_interval = intervals.pop(num)
        x = self._next_point[self._use_method](old_interval.GetILb()[0], old_interval.GetIRb()[0], old_interval.GetILb()[1], \
            old_interval.GetIRb()[1], lipsh)
        y = self.Func(x)
        self._sol.points.append((x, y))
        self.__UpdateMinValue((x, y))
        new_interval_l = interval(old_interval.GetILb(), (x, y)) 
        new_interval_r = interval((x, y), old_interval.GetIRb())

        method(new_interval_l, lipsh)
        method(new_interval_r, lipsh)

        new_intervals_1 = intervals[:num]
        new_intervals_2 = []

        if num != len(intervals):
            new_intervals_2 = intervals[num:]
        intervals = new_intervals_1
        intervals.extend([new_interval_l, new_interval_r])
        intervals.extend(new_intervals_2)
        return intervals

    def __CheckStop(self, _interval):
        return True if _interval.GetIRb()[0] - _interval.GetILb()[0] < self._eps else False

    def Minimize(self, lb, rb, r, method, max_iter=None, eps=None):
        intervals = list()
        lipsh = None

        if self.__CorrectnessParameters(lb, rb, r, max_iter, method):
            self.__InitializeData(lb, rb, r, max_iter, method, eps)
        else:
            raise TypeError("Invalid type of parameters")

        method = self._methods[method]
        initial_intervals = interval((lb, self.Func(lb)), (rb, self.Func(rb)))
        self._sol.points.append((lb, self.Func(lb)))
        self._sol.points.append((rb, self.Func(rb)))
        self.__UpdateMinValue(initial_intervals.GetILb(), initial_intervals.GetIRb())
        intervals.append(initial_intervals)
        while True:
            if self._spent_iter == self._max_iter:
                self._sol.minimum = self._minimum
                return self._sol
            if type(intervals) is int:
                self._sol.minimum = self._minimum
                return self._sol
            self.__IncreaseIterCount()
            self._sol.spent_iter = self._spent_iter
            lipsh = self.__GetLipsh(intervals)
            for iterv in intervals:
                method(iterv, lipsh)
            intervals = self.__GetNewIntervals(intervals, lipsh, method)
