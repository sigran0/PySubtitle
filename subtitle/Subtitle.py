
from abc import *
import os.path as path
import itertools


class Subtitle(metaclass=ABCMeta):

    CONVERT_TYPE = ('srt', 'SRT', 'vtt', 'VTT')

    def __init__(self, _sub_=None):
        self._subtitle_ = list()
        self._is_initialized_ = False

        if _sub_ is not None:
            self._subtitle_ = _sub_
            self._is_initialized_ = True

    @abstractmethod
    def _read_file(self, file_path, encoding='utf-8', lang='ENCC'):
        self._check_file_path(file_path)
        pass

    @abstractmethod
    def parse(self, file_path, encoding='utf-8'):
        self._is_initialized_ = True
        pass

    @abstractmethod
    def make_file(self, file_path, sub_range=None, encoding='utf-8'):
        self._check_initialized()
        pass

    @abstractmethod
    def convert_to(self, target_type):
        self._check_convert_target_type(target_type)
        pass

    def _set_subtitle_(self, _subtitle):
        self._is_initialized_ = True
        self._subtitle_ = _subtitle

    def _check_time_tuple(self, time_tuple):
        if type(time_tuple) is not tuple or len(time_tuple) != 4:
            raise ValueError('time object must be tuple and it has only 4 parameters: (h, m, s, msec)')

    def _check_file_path(self, file_path):
        if path.isfile(file_path) is not True:
            raise ValueError('please give valid file path')

    def _check_initialized(self):
        if self._is_initialized_ is False:
            raise ValueError('please parse subtitle file first')

    def _check_convert_target_type(self, target_type):
        if target_type not in self.CONVERT_TYPE:
            raise ValueError('{} type does not support on this plugin'.format(target_type))