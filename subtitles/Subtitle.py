
from abc import *
import os.path as path


class Subtitle(metaclass=ABCMeta):

    def __init__(self):
        self.lines = list()

    @abstractmethod
    def read_file(self, file_path):
        self._check_file_path(file_path)
        pass

    def _check_time_tuple(self, time_tuple):
        if type(time_tuple) is not tuple or len(time_tuple) != 4:
            raise ValueError('time object must be tuple and it has only 4 parameters: (h, m, s, msec)')

    def _check_file_path(self, file_path):
        if path.isfile(file_path) is not True:
            raise ValueError('please give valid file path')

    def get_hmsms(self, time_tuple, _format='{}:{}:{}.{}'):
        #   (hour, min, sec, milsec)
        self._check_time_tuple(time_tuple)
        string_list = []

        string_list.append(self.numbering(time_tuple[0]))
        string_list.append(self.numbering(time_tuple[1]))
        string_list.append(self.numbering(time_tuple[2]))
        string_list.append(self.numbering(str(time_tuple[3])[:3], size_of_zero=3))

        return _format.format(*string_list)

    def get_subtitle(self):
        return '\n'.join(self.lines)

    def make_subtitle(self, file_path):
        with open(file_path, 'w') as wf:
            subtitle_string = self.get_subtitle()
            wf.writelines(subtitle_string)

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