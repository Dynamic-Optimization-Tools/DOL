class opt(object):
    lb = None
    rb = None
    r = None
    max_iter = 1000
    
    def __init__(self):
        pass

    def __CorrectnessParameters(_lb, _rb, _r, _max_iter):
        if type(_lb) not is float or type(_rb) not is float \
            or type(_r) not is float or type(_max_iter) not is int \
                and type(_max_iter) not is None:
            return False
        return True

    def __SetLb(_lb):
        self.lb = _lb
    
    def __SetRb(_rb):
        self.rb = _rb

    def __SetR(_r):
        self.r = _r

    def __SetMaxIter(_max_iter):
        self.max_iter = _max_iter

    def __InitializeData(_lb, _rb, _r, _max_iter):
        __SetLb(_lb)
        __SetRb(_rb)
        __SetR(_r)
        if _max_iter not in None:
            __SetMaxIter(_max_iter)

    def __Piyavsky(self, _lip, _lb, _rb, _yl, _yr):
        return 0.5 * _lip * (_rb - _lb) - 0.5 * (_yr - _yl)

    def __Strongin(self, lip, lb, rb, yl, yr):
        return _lip * (_rb - _lb) + ((_yr - _yl)**2) / (_lip * (_rb - _lb)) \
            -2 * (_yr - _yl)

    def Minimize(self, lb, rb, r, func, max_iter=None):
        if __CorrectnessParameters(lb, rb, r, max_iter):
            __InitializeData(lb, rb, r, max_iter)
        return
 