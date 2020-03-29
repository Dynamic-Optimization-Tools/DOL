import math
import os
import sys
from os.path import dirname as up
root_dir = os.path.join(up(os.path.abspath(os.curdir)))
sys.path.insert(0, root_dir)
from src.interval import interval

class opt(object):
    lb = None
    rb = None
    r = None
    max_iter = 100
    minimum = (None, None)
    spent_iter = 0
    eps = 0.0001
    methods = { 
               "piyavsky": interval.GetPiyavskyCharacteristic,
               "strongin": interval.GetStronginCharacteristic
              }
    
    def __init__(self):
        pass

    def __CorrectnessParameters(self, _lb, _rb, _r, _max_iter):
        if type(_lb) is not float or type(_rb) is not float \
            or type(_r) is not float or type(_max_iter) is not int \
                and _max_iter is not None:
            return False
        return True

    def __SetLb(self, _lb):
        self.lb = _lb
    
    def __SetRb(self, _rb):
        self.rb = _rb

    def __SetR(self, _r):
        self.r = _r

    def __SetSpentIter(self, _spent_iter):
        self.spent_iter = _spent_iter

    def __SetMaxIter(self, _max_iter):
        self.max_iter = _max_iter

    
    def __SetMin(self, _min):
        self.minimum = _min

    def __InitializeData(self, _lb, _rb, _r, _max_iter):
        self.__SetLb(_lb)
        self.__SetRb(_rb)
        self.__SetR(_r)
        if _max_iter is not None:
            self.__SetMaxIter(_max_iter)

    def TestFunc(self, x):
        #return math.sin(x) * math.cos(x)
        #return x**2
        #return x
        #return 2 * math.sin(3 * x) + 3 * math.cos(5 * x)
        return (x-1)**2 

    def __UpdateMinValue(self, *args):
        #for i in args:
        #    print(i)
        #print("===========================")
        if self.minimum == (None, None):
            self.__SetMin(args[0])
        for arg in args:
            if self.minimum[1] > arg[1]:
                self.__SetMin(arg)

    def __IncreaseIterCount(self):
        self.__SetSpentIter(self.spent_iter + 1)


    def __GetLipsh(self, _intervals):
        _M = None
        for i, i_interval in enumerate(_intervals):
            for j, j_interval in enumerate(_intervals[i:]):
                _M_interval = abs((j_interval.GetIRb()[1] - i_interval.GetILb()[1]) / (j_interval.GetIRb()[0] - i_interval.GetILb()[0]))
                if _M is None:
                    _M = _M_interval
                else:
                    _M = _M_interval if _M < _M_interval else _M
        print("Lipshitz const = ", self.r * _M)
        return 1 if _M == 0 else self.r * _M

    def __GetBestInterval(self, _intervals):
        max_charact = _intervals[0].GetIR()
        num_interval = 0
        for num, interval in enumerate(_intervals):
            if max_charact < interval.GetIR():
                max_charact = interval.GetIR()
                num_interval = num
        return num_interval

    def PrintIntervals(self, intervals):
        s = ""
        for interval in intervals:
            s += "( " + str(interval.GetILb()[0]) + "; " +   str(interval.GetIRb()[0]) + " )"
        s += '\n'
        print(s)

    def __GetNextPoint(self, _intervals, _lipsh, _method):
        _num = self.__GetBestInterval(_intervals)
        self.PrintIntervals(_intervals)
        if self.__CheckStop(_intervals[_num]):
            return 0
        _old_interval = _intervals.pop(_num)
        _x = 0.5 * (_old_interval.GetIRb()[0] + _old_interval.GetILb()[0]) - 0.5 * ((_old_interval.GetIRb()[1] - _old_interval.GetILb()[1]) / _lipsh)
        print("Next x = ", _x)
        _y = self.TestFunc(_x)
        self.__UpdateMinValue((_x,_y))
        _new_interval_l = interval(_old_interval.GetILb(), (_x, _y)) 
        _new_interval_r = interval((_x, _y), _old_interval.GetIRb())

        _method(_new_interval_l, _lipsh)
        _method(_new_interval_r, _lipsh)

        new_intervals_1 = _intervals[:_num]
        new_intervals_2 = []

        if _num != len(_intervals):
            new_intervals_2 = _intervals[_num + 1:]
        _intervals = new_intervals_1
        _intervals.extend([_new_interval_l, _new_interval_r])
        _intervals.extend(new_intervals_2)

        self.PrintIntervals(_intervals)
        return _intervals

    def __CheckStop(self, _interval):
        return True if _interval.GetIRb()[0] - _interval.GetILb()[0] < self.eps else False

    def Minimize(self, lb, rb, r, func, method, max_iter=None):
        intervals = list()
        _lipsh = None
        _method = self.methods[method]

        if self.__CorrectnessParameters(lb, rb, r, max_iter):
            self.__InitializeData(lb, rb, r, max_iter)
        else:
            raise TypeError("Invalid type of parameters")
        
        initial_intervals = interval((lb, self.TestFunc(lb)), (rb, self.TestFunc(rb)))
        self.__UpdateMinValue(initial_intervals.GetILb(), initial_intervals.GetIRb())
        intervals.append(initial_intervals)
        while True:
            if self.spent_iter == self.max_iter:
                return (self.minimum, self.spent_iter)
            if type(intervals) is int:
                print(self.minimum)
                print(self.spent_iter)
                return 0
            self.__IncreaseIterCount()
            _lipsh = self.__GetLipsh(intervals)
            for iterv in intervals:
                _method(iterv, _lipsh)
            intervals = self.__GetNextPoint(intervals, _lipsh, _method)
        return

a = opt()
a.Minimize(-1., 2., 2., "", "piyavsky")
print(a.minimum)