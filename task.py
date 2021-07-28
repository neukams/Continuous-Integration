'''
Authors: Spencer Neukam, Dustin Walkup, Michael Zimmerman
Description:
'''


def conv_num(num_str):
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

    return Number(num_str).numberfy()


def my_datetime(num_sec):
    '''
    Pending
    '''
    return "01-01-1970"


def conv_endian(num, endian):
    '''
    Pending
    '''
    return "0E 91 A2"
