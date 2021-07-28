'''
Authors:
Description:
'''
import unittest
from task import conv_num
from task import my_datetime
from task import conv_endian


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


if __name__ == '__main__':
    unittest.main()
