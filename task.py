'''
Authors:
Description:
'''


def conv_num(num_str):
    '''
    Pending
    '''
    return 12345


def my_datetime(num_sec):
    '''
    Pending
    '''
    return "01-01-1970"


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
