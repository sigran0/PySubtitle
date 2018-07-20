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


def get_hmsms(self, time_tuple, _format='{}:{}:{}.{}'):
    #   (hour, min, sec, milsec)
    self._check_time_tuple(time_tuple)
    string_list = []

    string_list.append(self.numbering(time_tuple[0]))
    string_list.append(self.numbering(time_tuple[1]))
    string_list.append(self.numbering(time_tuple[2]))
    string_list.append(self.numbering(str(time_tuple[3])[:3], size_of_zero=3))

    return _format.format(*string_list)


def numbering(self, num, size_of_zero=2):

    result_string = ''

    if size_of_zero < 0:
        raise ValueError('size_of_zero must be greater than 0')

    num_length = len(str(num))

    if num_length > size_of_zero:
        raise ValueError('length of number must be less than size_of_zero')

    for c in range(size_of_zero - num_length):
        result_string += '0'

    result_string += '{}'.format(num)

    return result_string