
from abc import *
import os.path as path
import itertools


class Subtitle(metaclass=ABCMeta):

    CONVERT_TYPE = ('srt', 'SRT', 'vtt', 'VTT', 'smi', 'SMI')

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

    def convert_to(self, target_type):
        #   TODO    abstactmethod 의 default 기능들이 작동을 하지 않는다..?
        # self._check_initialized()
        self._check_convert_target_type(target_type)

        if target_type in ('srt', 'SRT'):
            from subtitle.SRT import SRT
            return SRT(self._subtitle_)
        elif target_type in ('vtt', 'VTT'):
            from subtitle.VTT import VTT
            return VTT(self._subtitle_)
        elif target_type in ('smi', 'SMI'):
            from subtitle.SMI import SMI
            return SMI(self._subtitle_)

    def _get_sub_index(self, start_milsec, end_milsec):
        result_index_list = list()

        for sub in self._subtitle_:
            sub_start_milsec = self._hmsms_to_milsec_(sub['start_time'])
            sub_end_milsec = self._hmsms_to_milsec_(sub['end_time'])

            if sub_end_milsec > end_milsec:
                break

            if sub_start_milsec < start_milsec:
                continue

            result_index_list.append(sub['number'])

        return result_index_list

    def _get_sub_subtitle_list_(self, start_milsec, end_milsec):
        result_subtitle_list = list()
        sub_indies = self._get_sub_index(start_milsec, end_milsec)

        for c, sub_index in enumerate(sub_indies):
            target_subtitle = self._subtitle_[sub_index]
            target_subtitle['number'] = c + 1
            result_subtitle_list.append(target_subtitle)

        return result_subtitle_list

    def _hmsms_to_milsec_(self, hmsms):
        #   hour    : 60 * 60 * 1000
        #   min     : 60 * 1000
        #   sec     : 1000
        #   milsec  : 1
        return (hmsms[0] * 60 * 60 * 1000) + (hmsms[1] * 60 * 1000) + (hmsms[2] * 1000) + (hmsms[3])

    def _milsec_to_hmsms_(self, milsec):
        _hour = int(milsec / (60 * 60 * 1000))
        milsec -= _hour * (60 * 60 * 1000)

        _min = int(milsec / (60 * 1000))
        milsec -= _min * (60 * 1000)

        _sec = int(milsec / 1000)
        milsec -= _sec * 1000

        return _hour, _min, _sec, milsec

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