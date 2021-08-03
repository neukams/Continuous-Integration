'''
Authors: Spencer Neukam, Dustin Walkup, Michael Zimmerman
Description:
'''
import unittest
from task import conv_num
from task import my_datetime
from task import conv_endian


class TestConvNum(unittest.TestCase):

    def test_provided_by_assignment(self):
        self.assertEqual(conv_num(""), None)
        self.assertEqual(conv_num("12345"), 12345)
        self.assertEqual(conv_num("-123.45"), -123.45)
        self.assertEqual(conv_num(".45"), 0.45)
        self.assertEqual(conv_num("123."), 123.0)
        self.assertEqual(conv_num("0xAD4"), 2772)
        self.assertEqual(conv_num('12345A'), None)
        self.assertEqual(conv_num('12.3.45'), None)

    def test_no_hex_prefx(self):
        self.assertEqual(conv_num("AD4"), None)
        self.assertEqual(conv_num("1A"), None)

    def test_zero_prefix(self):
        self.assertEqual(conv_num("0001"), 1)
        self.assertEqual(conv_num("000.1"), 0.1)
        self.assertEqual(conv_num("0.0"), 0.0)
        self.assertEqual(conv_num("00xAD4"), None)
        self.assertEqual(conv_num("-0001"), -1)
        self.assertEqual(conv_num("-000.1"), -0.1)
        self.assertEqual(conv_num("-00xAD4"), None)

    def test_case_insensitivity(self):
        self.assertEqual(conv_num("0xAf"), 175)
        self.assertEqual(conv_num("0xaF"), 175)
        self.assertEqual(conv_num("0XAF"), 175)
        self.assertEqual(conv_num("0xaf"), 175)
        self.assertEqual(conv_num("0xAF"), 175)
        self.assertEqual(conv_num("-0xAf"), -175)
        self.assertEqual(conv_num("-0xaF"), -175)
        self.assertEqual(conv_num("-0XAF"), -175)
        self.assertEqual(conv_num("-0xaf"), -175)
        self.assertEqual(conv_num("-0xAF"), -175)

    def test_return_type(self):
        self.assertEqual(isinstance(conv_num("1"), int), True)
        self.assertEqual(isinstance(conv_num("0"), int), True)
        self.assertEqual(isinstance(conv_num("1."), float), True)
        self.assertEqual(isinstance(conv_num("1.0"), float), True)
        self.assertEqual(isinstance(conv_num(".0"), float), True)
        self.assertEqual(isinstance(conv_num("0xAF"), int), True)
        self.assertEqual(isinstance(conv_num("-0xAF"), int), True)

    def test_invalid_format(self):
        # Negative symbol checks.
        self.assertEqual(conv_num("--1"), None)
        self.assertEqual(conv_num("1-1"), None)
        self.assertEqual(conv_num("-99-"), None)
        self.assertEqual(conv_num("-9.-9"), None)
        self.assertEqual(conv_num("-0xA-F"), None)
        # Hexadecimal symbol checks.
        self.assertEqual(conv_num("xAF"), None)
        self.assertEqual(conv_num("x0AF"), None)
        self.assertEqual(conv_num("0xA0xF"), None)
        self.assertEqual(conv_num("0xAFG"), None)
        self.assertEqual(conv_num("0xxAF"), None)
        self.assertEqual(conv_num("0xAXF"), None)
        self.assertEqual(conv_num("0x-AF"), None)
        self.assertEqual(conv_num("0-xAF"), None)
        self.assertEqual(conv_num("0x0.AF"), None)
        self.assertEqual(conv_num(".0x0AF"), None)
        self.assertEqual(conv_num("-0x0.AF"), None)
        # Float symbol checks
        self.assertEqual(conv_num(".000."), None)
        self.assertEqual(conv_num("99..0"), None)
        self.assertEqual(conv_num("99.."), None)
        # Invalid symbol only
        self.assertEqual(conv_num("0x"), None)
        self.assertEqual(conv_num("."), None)
        self.assertEqual(conv_num("-"), None)

    def test_large_integer(self):
        self.assertEqual(conv_num(
            "100000000000000000000000000000000000000000001"),
            100000000000000000000000000000000000000000001)
        self.assertEqual(conv_num(
            "-100000000000000000000000000000000000000000001"),
            -100000000000000000000000000000000000000000001)

    def test_large_float(self):
        self.assertEqual(conv_num(
            "0.100000000000000000000000000000000000000000001"),
            0.100000000000000000000000000000000000000000001)
        self.assertEqual(conv_num(
            "-0.100000000000000000000000000000000000000000001"),
            -0.100000000000000000000000000000000000000000001)

    def test_large_hex(self):
        self.assertEqual(conv_num(
            "0x47BF19673DF52E37F2410011D100000000001"),
            100000000000000000000000000000000000000000001)
        self.assertEqual(conv_num(
            "-0x47BF19673DF52E37F2410011D100000000001"),
            -100000000000000000000000000000000000000000001)


class TestMyDatetime(unittest.TestCase):
    '''
    Pending
    '''

    def test_zero(self):
        '''
        Pending
        '''
        self.assertEqual(my_datetime(0), "01-01-1970")


class TestConvEndian(unittest.TestCase):
    '''
    Pending
    '''

    def test_big(self):
        '''
        Pending
        '''
        self.assertEqual(conv_endian(954786, "big"), "0E 91 A2")


if __name__ == '__main__':
    unittest.main()
