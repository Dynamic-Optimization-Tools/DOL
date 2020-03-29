import unittest
import sys
import os
from os.path import dirname as up
root_dir = os.path.join(up(os.path.abspath(os.curdir)))
sys.path.insert(0, root_dir)
from src.opt import opt


class ModuleTests(unittest.TestCase):
    def test_ExceptOnInvalidRParam(self):
        # Initialization
        class_obj = opt()
        lb = 0.0
        rb = 1.0
        r = "1"
        func = ""
        max_iter = 1 
        # Action

        # Validation
        self.assertRaises(TypeError, class_obj.Minimize, rb, lb, r, func, max_iter)


    def test_ExceptOnInvalidLbParam(self):
        # Initialization
        class_obj = opt()
        lb = "0."
        rb = 1.0
        r = 1.0
        func = ""
        max_iter = 1    
        # Action

        # Validation
        self.assertRaises(TypeError, class_obj.Minimize, rb, lb, r, func, max_iter)


    def test_ExceptOnInvalidRbParam(self):
        # Initialization
        class_obj = opt()
        lb = 0.0
        rb = "1.0"
        r = 1.0
        func = ""
        max_iter = 1    
        # Action

        # Validation
        self.assertRaises(TypeError, class_obj.Minimize, rb, lb, r, func, max_iter)

    
    def test_ExceptOnInvalidMaxIterParam(self):
        # Initialization
        class_obj = opt()
        lb = 0.0
        rb = 1.0
        r = 1.0
        func = ""
        max_iter = "1"  
        # Action

        # Validation
        self.assertRaises(TypeError, class_obj.Minimize, rb, lb, r, func, max_iter)

    def test_DoesNotRaiseOnNoneMaxIter(self):
        # Initialization
        class_obj = opt()
        lb = 0.0
        rb = 1.0
        r = 1.0
        func = ""
        max_iter = None
        raise_except = False
        # Action
        try:
            class_obj.Minimize(rb, lb, r, func, max_iter)
        except:
            raise_except = True
        # Validation
        self.assertEqual(False, raise_except)
        

if __name__ == '__main__':
    unittest.main()

