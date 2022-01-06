import unittest
import calc

def add(x,y):
    return x+y

def divide(x,y):
    return x/y


class TestCalc(unittest, TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(-1,5),15)
        self.assertEqual(calc.add(10,6), 15)
    
    def test_divide(self):
        self.assertEqual(calc.divide(10,5),2)
        self.assertEqual(calc.add(-1,1),-1)
        self.assertEqual(calc.add(-1,-1), 1)

if __name__ == '__main__':
    unittest.main()