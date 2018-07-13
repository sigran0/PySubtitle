
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
