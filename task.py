'''
Authors: Spencer Neukam, Dustin Walkup, Michael Zimmerman
Description:
'''


def conv_num(num_str):
    return Number(num_str).numberfy()


def my_datetime(seconds: int) -> str:
    """
    Returns a date in string format ('MM-DD-YYYY')
    given the seconds since epoch
    :param: seconds: int, number of seconds since epoch
    :return: string: date 'MM-DD-YYY'
    """

    # variables
    DAYS_IN_COMMON_MONTH = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31,
                            8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    DAY = 86400
    year = 1970
    month = 1
    day = 1

    # calculate year
    while True:

        # get the number of seconds in this year
        if (year % 4 != 0) or \
                (year % 4 == 0 and year % 100 == 0 and year % 400 != 0):
            add_year = DAY * 365
        else:
            add_year = DAY * 366

        # exit criteria
        if seconds - add_year < 0:
            break

        # add a year
        seconds -= add_year
        year += 1

    # calculate month
    while True:

        # get the number of seconds in this month
        if month == 2 and \
                (
                        ((year % 4 == 0) and (year % 100 != 0))
                        or
                        ((year % 4 == 0) and (
                                year % 100 == 0 and year % 400 == 0))
                ):
            add_month = DAY * 29
        else:
            add_month = DAY * DAYS_IN_COMMON_MONTH[month]

        # exit criteria
        if seconds - add_month < 0:
            break

        seconds -= add_month
        month += 1

    # calculate day
    while True:
        if seconds - DAY < 0:
            break
        seconds -= DAY
        day += 1

    # return
    return str(twoDigitInt(month)) + "-" + str(twoDigitInt(day)) + "-" + \
        str(year)


def conv_endian(num, endian='big'):
    """
    accepts integer and endian type and returns a hexadcimal string
    """
    endian = endian.lower()

    # if the endian value is something other than big or little, return none
    if (endian != 'big') and (endian != 'little'):
        return None

    negative = False

    # if integer is negative, make it positive set negative boolean to True
    if num < 0:
        num *= -1
        negative = True

    # calls function that returns hexadecimal number string
    hex_string = int_to_hex(num)

    # if endian is little, call conv_little_endian function to convert from big
    # to little endian
    if endian == 'little':
        hex_string = conv_little_endian(hex_string)

    # strip string of any additional whitespace
    hex_string = hex_string.strip()

    # if integer was negative, add negative sign to hex number string
    if negative:
        hex_string = '-' + hex_string

    return hex_string


def int_to_hex(num):
    """
    accepts integer returns hex number string with two character bytes spaces
    """
    if num == 0:
        return '00'

    # dictionary that will convert digits to hex number
    hex_dic = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
               8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E',
               15: 'F'}

    hex_string = ''
    space_count = 0
    char_count = 0

    # converts each digit to its hex counterpart, concatenates it to hex_string
    while num > 0:
        remainder = num % 16
        hex_char = hex_dic.get(remainder)
        hex_string = hex_char + hex_string
        space_count += 1
        char_count += 1

        # adds a space every 2 chars
        if space_count == 2:
            hex_string = ' ' + hex_string
            space_count = 0

        num = num // 16

    # if hex string digits are odd, add a zero to beginning of string
    if char_count % 2 != 0:
        hex_string = '0' + hex_string

    return hex_string


def conv_little_endian(hex_string):
    """
    converts big endian to little endian hex number
    """
    temp_string = ''

    while hex_string != '':
        last_two = hex_string[-2:]
        temp_string = temp_string + last_two + " "
        hex_string = hex_string[:-3]
    return temp_string


class Number:
    '''
    This class accepts a Python string value, validates if the input
    represents a hexadecimal, float, or integer value, and computes the
    corresponding numerical value.
    '''

    def __init__(self, cn_str):
        self.input_str = cn_str
        self.input_str_len = len(self.input_str)
        self.idx = 0
        self.isNegative = False
        self.isHexadecimal = False
        self.decimalIdx = -1
        self.tokens = []
        self.base = 10
        self.output_num = 0

    def testHyphen(self):
        '''
        Validate hyphen placement and string length.
        '''
        if self.idx != 0 or self.input_str_len == 1:
            return False

        self.isNegative = True

        return True

    def testHexPrefix(self):
        '''
        Validate hexadecimal prefix: '0x..' or '-0x..' and string length.
        '''
        xIdx = 1
        if self.isNegative:
            xIdx = 2

        if self.idx != xIdx or self.input_str[self.idx - 1] != '0':
            return False
        if self.input_str_len == xIdx + 1:
            return False

        # Zero will be the first element in tokens and is actually a
        # symbol. In this scenario we remove the 0 digit and start with
        # next number.
        del self.tokens[0]
        self.base = 16
        self.isHexadecimal = True

        return True

    def testDecimal(self):
        '''
        Validate single decimal point and string length.
        '''
        if self.isHexadecimal:
            return False
        if self.decimalIdx != -1 or self.input_str_len == 1:
            return False

        if self.isNegative:
            # We do not include the '-' symbol in tokens[]. We must shift
            # decimal index to align with digits in tokens[].
            self.decimalIdx = self.idx - 1
        else:
            self.decimalIdx = self.idx

        return True

    def hexA(self):
        if not self.isHexadecimal:
            return False
        return 10

    def hexB(self):
        if not self.isHexadecimal:
            return False
        return 11

    def hexC(self):
        if not self.isHexadecimal:
            return False
        return 12

    def hexD(self):
        if not self.isHexadecimal:
            return False
        return 13

    def hexE(self):
        if not self.isHexadecimal:
            return False
        return 14

    def hexF(self):
        if not self.isHexadecimal:
            return False
        return 15

    def lexer(self):
        '''
        Lexer will iterate through each character of input string and is
        responsible for:
        (1) Validating that input string represents a hexadecimal, float,
            or integer value.
        (2) Populate a list of numerical "tokens" representing the input.
        '''
        # Only allow these characters.
        cases = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'A': self.hexA,
            'B': self.hexB,
            'C': self.hexC,
            'D': self.hexD,
            'E': self.hexE,
            'F': self.hexF,
            'X': self.testHexPrefix,
            '.': self.testDecimal,
            '-': self.testHyphen
        }

        # Test for empty string
        if self.input_str_len == 0:
            return None

        for ch in self.input_str:
            digit = cases.get(ch.upper())

            # If symbol ('X', '.', '-') call function.
            if callable(digit):
                digit = digit()

            # Validate result of 'get' lookup.
            if digit is None:
                return None
            if digit is False and isinstance(digit, bool):
                return None
            # Skip/do not append symbol to token list.
            if digit is True and isinstance(digit, bool):
                self.idx += 1
                continue

            self.tokens.append(digit)
            self.idx += 1

        return self.tokens

    def get_number(self):
        '''
        Iterates through "tokens" and calculates numerical output.
        '''
        end = self.input_str_len
        value = 0

        # If Float, calculate decimal portion separately.
        if self.decimalIdx != -1:
            self.get_decimal()
            end = self.decimalIdx

        # Calculate value for base10 or base16.
        for digit in self.tokens[:end]:
            value *= self.base
            value += digit
        self.output_num += value

        if self.isNegative:
            self.output_num *= -1

        return self.output_num

    def get_decimal(self):
        '''
        Iterates through "tokens" decimal portion and calculates numerical
        output.
        '''
        place = 1
        value = 0.0

        for digit in self.tokens[self.decimalIdx:]:
            value += digit / (10 ** place)
            place += 1

        self.output_num += value

    def numberfy(self):
        '''
        Orchestration function that ensures correct order of operations for
        function calls.
        '''
        if self.lexer() is None:
            return None

        return self.get_number()


def twoDigitInt(num: int) -> str:
    """
    Given an integer between 1 and 99, convert it to a two-digit string
    If applicable, add a leading zero
    ex: 4 -> '04'
    ex: 12 -> '12'
    :param: num, a two-digit integer
    :return: string
    """

    if num < 1 or num > 99:
        return "error"
    elif num < 10:
        return str(0) + str(num)
    return str(num)
