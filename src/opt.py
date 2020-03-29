class opt(object):
    lb = None
    rb = None
    r = None
    max_iter = 1000
    
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

    def __SetMaxIter(self, _max_iter):
        self.max_iter = _max_iter

    def __InitializeData(self, _lb, _rb, _r, _max_iter):
        self.__SetLb(_lb)
        self.__SetRb(_rb)
        self.__SetR(_r)
        if _max_iter is not None:
            self.__SetMaxIter(_max_iter)

    def __Piyavsky(self, _lip, _lb, _rb, _yl, _yr):
        return 0.5 * _lip * (_rb - _lb) - 0.5 * (_yr - _yl)

    def __Strongin(self, _lip, _lb, _rb, _yl, _yr):
        return _lip * (_rb - _lb) + ((_yr - _yl)**2) / (_lip * (_rb - _lb)) \
            -2 * (_yr - _yl)

    def Minimize(self, lb, rb, r, func, max_iter=None):
        if self.__CorrectnessParameters(lb, rb, r, max_iter):
            self.__InitializeData(lb, rb, r, max_iter)
        else:
            raise TypeError("Invalid type of parameters")
        return
 