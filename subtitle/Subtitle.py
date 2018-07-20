
from abc import *
import os.path as path
import itertools


class Subtitle(metaclass=ABCMeta):

    def __init__(self):
        self._subtitle = list()

    @abstractmethod
    def _read_file(self, file_path, encoding='utf-8'):
        self._check_file_path(file_path)
        pass

    @abstractmethod
    def parse(self, file_path, encoding='utf-8'):
        pass

    @abstractmethod
    def make_file(self, file_path, encoding='utf-8'):
        pass

    def _check_time_tuple(self, time_tuple):
        if type(time_tuple) is not tuple or len(time_tuple) != 4:
            raise ValueError('time object must be tuple and it has only 4 parameters: (h, m, s, msec)')

    def _check_file_path(self, file_path):
        if path.isfile(file_path) is not True:
            raise ValueError('please give valid file path')