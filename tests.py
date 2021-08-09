'''
Authors: Spencer Neukam, Dustin Walkup, Michael Zimmerman
'''
import unittest
from task import conv_num
from task import my_datetime
from task import conv_endian
import random


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
    """
    Test Class for the my_datetime() function
    """

    def test_zero(self):
        """
        0 seconds since epoch should return epoch
        """
        self.assertEqual(my_datetime(0), "01-01-1970")

    def test_canvas_examples(self):
        """
        Canvas example tests
        """
        self.assertEqual(my_datetime(123456789), "11-29-1973")
        self.assertEqual(my_datetime(9876543210), "12-22-2282")
        self.assertEqual(my_datetime(201653971200), "02-29-8360")

    def random_testing(self):
        """
        Random testing
        """
        self.assertEqual(my_datetime(15658919219), "03-18-2466")
        self.assertEqual(my_datetime(87441747538), "12-02-4740")
        self.assertEqual(my_datetime(180554127899), "07-13-7691")
        self.assertEqual(my_datetime(30578684726), "12-31-2938")
        self.assertEqual(my_datetime(104203010137), "01-23-5272")
        self.assertEqual(my_datetime(169420530963), "09-21-7338")
        self.assertEqual(my_datetime(105140905211), "10-13-5301")
        self.assertEqual(my_datetime(175800114903), "11-19-7540")
        self.assertEqual(my_datetime(162283651159), "07-25-7112")
        self.assertEqual(my_datetime(154249369071), "12-19-6857")
        self.assertEqual(my_datetime(163297868897), "09-14-7114")
        self.assertEqual(my_datetime(23588344039), "06-27-2717")
        self.assertEqual(my_datetime(130622646521), "04-08-6109")
        self.assertEqual(my_datetime(12974675870), "02-24-2381")
        self.assertEqual(my_datetime(83076822877), "09-08-4602")
        self.assertEqual(my_datetime(151727270369), "01-17-6778")
        self.assertEqual(my_datetime(142695209990), "10-30-6491")
        self.assertEqual(my_datetime(48667988133), "03-24-3512")
        self.assertEqual(my_datetime(47729571464), "06-28-3482")
        self.assertEqual(my_datetime(76749863467), "02-08-4402")
        self.assertEqual(my_datetime(36924182774), "01-31-3140")
        self.assertEqual(my_datetime(162929327398), "01-10-7133")


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
