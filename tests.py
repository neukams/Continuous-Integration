'''
Authors:
Description:
'''
import unittest
from task import conv_num
from task import my_datetime
from task import conv_endian
import random


class TestConvNum(unittest.TestCase):
    '''
    Pending
    '''

    def test_conv_num_positive_int(self):
        '''
        Pending
        '''
        self.assertEqual(conv_num("12345"), 12345)


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

    def test1(self):
        var = 954786
        expected = "0E 91 A2"
        self.assertEqual(conv_endian(var), expected)

    def test2(self):
        var = -954786
        expected = "-0E 91 A2"
        self.assertEqual(conv_endian(var), expected)

    def test3(self):
        var = 954786
        expected = "A2 91 0E"
        self.assertEqual(conv_endian(var, 'little'), expected)

    def test4(self):
        var = 954786
        expected = None
        self.assertEqual(conv_endian(var, 'small'), expected)

    # random testing
    def test5(self):
        min_int = -2147483648
        max_int = 2147483647
        for i in range(0, 500):
            endian_value = random.randint(0, 1)
            endian_value = 'big' if endian_value == 1 else 'little'
            var = random.randint(min_int, max_int)
            conv_endian(var, endian_value)

    def test6(self):
        var = 14
        expected = '0E'
        self.assertEqual(conv_endian(var, 'little'), expected)

    def test7(self):
        var = 0
        expected = '00'
        self.assertEqual(conv_endian(var), expected)

    def test8(self):
        var = 2147483647
        expected = '7F FF FF FF'
        self.assertEqual(conv_endian(var), expected)

    def test9(self):
        var = -2147483648
        expected = '-00 00 00 80'
        self.assertEqual(conv_endian(var, 'little'), expected)

    def test10(self):
        var = 954786
        expected = "A2 91 0E"
        self.assertEqual(conv_endian(var, 'LitTle'), expected)


if __name__ == '__main__':
    unittest.main()
