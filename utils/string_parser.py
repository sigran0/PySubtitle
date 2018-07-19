from functools import reduce


def _string_to_number(target):
    number = 0
    size = len(target) - 1
    for c, num in enumerate(target):
        mul = 10 ** (size - c)
        number += int(num) * mul
    return number


def _string_to_time_string(target):
    return _string_to_number(target[0:2]), _string_to_number(target[3:5]), \
           _string_to_number(target[6:8]), _string_to_number(target[9:])


def parse_time_string(time_string):
    start_time_string, end_time_string = time_string.split(' --> ')
    return (_string_to_time_string(start_time_string), _string_to_time_string(end_time_string))


def lines_to_string(target, newline=''):
    return str(reduce(lambda x, y: x + newline + y, target))