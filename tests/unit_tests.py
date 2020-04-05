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
        rb = 8.0
        r = "1"
        method = "piyavsky"
        max_iter = 1
        # Action

        # Validation
        self.assertRaises(TypeError, class_obj.Minimize, lb, rb, r, method, max_iter)


    def test_ExceptOnInvalidLbParam(self):
        # Initialization
        class_obj = opt()
        lb = "0."
        rb = 1.0
        r = 1.0
        method = "piyavsky"
        max_iter = 1    
        # Action

        # Validation
        self.assertRaises(TypeError, class_obj.Minimize, lb, rb, r, method, max_iter)


    def test_ExceptOnInvalidRbParam(self):
        # Initialization
        class_obj = opt()
        lb = 0.0
        rb = "1.0"
        r = 1.0
        method = "piyavsky"
        max_iter = 1    
        # Action

        # Validation
        self.assertRaises(TypeError, class_obj.Minimize, lb, rb, r, method, max_iter)

    
    def test_ExceptOnInvalidMaxIterParam(self):
        # Initialization
        class_obj = opt()
        lb = 0.0
        rb = 1.0
        r = 1.0
        method = "piyavsky"
        max_iter = "1"  
        # Action

        # Validation
        self.assertRaises(TypeError, class_obj.Minimize, lb, rb, r, method, max_iter)

    def test_DoesNotRaiseOnNoneMaxIter(self):
        # Initialization
        class_obj = opt()
        lb = 0.0
        rb = 8.0
        r = 2.0
        method = "piyavsky"
        max_iter = None
        raise_except = False
        # Action
        try:
            class_obj.Minimize(lb, rb, r, method, max_iter)
        except:
            raise_except = True
        # Validation
        self.assertEqual(False, raise_except)

    def test_CorrectMinFuncValuePiyavsky(self):
        # Initialization
        class_obj = opt()
        lb = 0.0
        rb = 8.0
        r = 2.0
        expected_func_value = -4.92057565
        method = "piyavsky"
        max_iter = 800
        # Action
        class_obj.Minimize(lb, rb, r, method, max_iter)
        # Validation
        self.assertAlmostEqual(class_obj.minimum[1], expected_func_value)

    def test_CorrectMinFuncValueStrongin(self):
        # Initialization
        class_obj = opt()
        lb = 0.0
        rb = 8.0
        r = 2.0
        expected_func_value = -4.920616335
        method = "strongin"
        max_iter = 800
        # Action
        class_obj.Minimize(lb, rb, r, method, max_iter)
        # Validation
        self.assertAlmostEqual(class_obj.minimum[1], expected_func_value)
        

if __name__ == '__main__':
    unittest.main()

