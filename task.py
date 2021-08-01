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
    if (endian != 'big') and (endian != 'little'):
        return None

    negative = False

    if num < 0:
        num *= -1
        negative = True

    hex_string = int_to_hex(num)

    if endian == 'little':
        temp_string = ''

        while hex_string != '':
            last_two = hex_string[-2:]
            temp_string = temp_string + last_two + " "
            hex_string = hex_string[:-3]

        hex_string = temp_string.strip()

    if negative:
        hex_string = '-' + hex_string

    return hex_string


def int_to_hex(num):

    hex_dic = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
               8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    hex_string = ''
    space_count = 0

    while num > 0:
        remainder = num % 16
        hex_char = hex_dic.get(remainder)
        hex_string = hex_char + hex_string
        space_count += 1

        if space_count == 2:
            hex_string = ' ' + hex_string
            space_count = 0

        num = num // 16

    if len(hex_string) % 2 != 0:
        hex_string = '0' + hex_string

    return hex_string
