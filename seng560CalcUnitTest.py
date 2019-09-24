import unittest
import seng560Calc

class TestCalcMethods(unittest.TestCase):

    def test_add(self):
        self.assertEqual(1, seng560Calc.add(0,1))
        self.assertEqual(None, seng560Calc.add('dog','cat'))
        
    def test_subtract(self):
        self.assertEqual(0, seng560Calc.subtract(1,1))
        self.assertEqual(None, seng560Calc.subtract('dog','cat'))
        
    def test_multiply(self):
        self.assertEqual(4, seng560Calc.multiply(2,2))
        self.assertEqual(None, seng560Calc.multiply('dog','cat'))
        
    def test_divide(self):
        self.assertEqual(2, seng560Calc.divide(4,2))
        self.assertEqual(None, seng560Calc.divide('dog','cat'))
        
    def test_squareroot(self):
        self.assertEqual(3, seng560Calc.squareroot(9))
        self.assertEqual(None, seng560Calc.squareroot('dog'))
        
    def test_exponent(self):
        self.assertEqual(16, seng560Calc.exponent(4,2))
        self.assertEqual(None, seng560Calc.exponent('dog','cat'))
        
    def test_convertToInt(self):
        self.assertEqual(1, seng560Calc.convertToInt(1.5))
        self.assertEqual(241, seng560Calc.convertToInt(0xf1))
        self.assertEqual(241, seng560Calc.convertToInt('0xf1'))
        self.assertEqual(49, seng560Calc.convertToInt(0O61))
        self.assertEqual(49, seng560Calc.convertToInt('0O61'))
        self.assertEqual(3, seng560Calc.convertToInt(0b11))
        self.assertEqual(3, seng560Calc.convertToInt('0b11'))
        
    def test_convertToHex(self):
        self.assertEqual(None, seng560Calc.convertToHex(1.5))
        self.assertEqual('0xf', seng560Calc.convertToHex(15))
        self.assertEqual('0x31', seng560Calc.convertToHex(0O61))
        self.assertEqual('0x31', seng560Calc.convertToHex('0O61'))
        self.assertEqual('0x3', seng560Calc.convertToHex(0b11))
        self.assertEqual('0x3', seng560Calc.convertToHex('0b11'))
        
    def test_convertToOct(self):
        self.assertEqual(None, seng560Calc.convertToOct(1.5))
        self.assertEqual('0o7', seng560Calc.convertToOct(7))
        self.assertEqual('0o61', seng560Calc.convertToOct(0x31))
        self.assertEqual('0o61', seng560Calc.convertToOct('0x31'))
        self.assertEqual('0o3', seng560Calc.convertToOct(0b11))
        self.assertEqual('0o3', seng560Calc.convertToOct('0b11'))
        
    def test_convertToBin(self):
        self.assertEqual(None, seng560Calc.convertToBin(1.5))
        self.assertEqual('0b111', seng560Calc.convertToBin(7))
        self.assertEqual('0b1111', seng560Calc.convertToBin(0xF))
        self.assertEqual('0b1111', seng560Calc.convertToBin('0xF'))
        self.assertEqual('0b1001', seng560Calc.convertToBin(0o11))
        self.assertEqual('0b1001', seng560Calc.convertToBin('0O11'))

if __name__ == '__main__':
    unittest.main()