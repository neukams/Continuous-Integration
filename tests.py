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
