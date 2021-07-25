import unittest
from task import conv_num
from task import my_datetime
from task import conv_endian


class Test_conv_num(unittest.TestCase):

    def test_conv_num_positive_int(self):
        self.assertEqual(conv_num("12345"), 12345)


class Test_my_datetime(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(my_datetime(0), "01-01-1970")


class Test_conv_endian(unittest.TestCase):

    def test_big(self):
        self.assertEqual(conv_endian(954786, "big"), "0E 91 A2")


if __name__ == '__main__':
    unittest.main()
