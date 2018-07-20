
from subtitle.Subtitle import Subtitle
from samitizer import Smi
from utils.string_parser import parse_time_string
from utils.string_parser import lines_to_string


class SMI(Subtitle):

    def __init__(self, _sub_=None):
        Subtitle.__init__(self, _sub_=_sub_)

    def _read_file(self, file_path, encoding='utf-8', lang='ENCC'):
        smi = Smi(file_path)
        return smi.convert('vtt', lang=lang)

    def convert_to(self, target_type):

        if target_type in ('srt', 'SRT'):
            from subtitle.SRT import SRT
            return SRT(self._subtitle_)
        elif target_type in ('vtt', 'VTT'):
            from subtitle.VTT import VTT
            return VTT(self._subtitle_)

    def parse(self, file_path, encoding='utf-8'):
        lines = self._read_file(file_path, encoding)
        target_string = lines_to_string(lines)
        target_string = target_string.replace('WEBVTT\n\n', '')
        target_string = target_string.replace('WEBVTT\n', '')
        target_string = target_string.replace('WEBVTT', '')

        subtitle_packs = target_string.split('\n\n')

        for subtitle_pack in subtitle_packs:

            if len(subtitle_pack) == 0:
                break

            lines = subtitle_pack.split('\n')

            number = int(lines[0])
            (start_time, end_time) = parse_time_string(lines[1])
            subtitle_text = lines_to_string(lines[2:], newline='\n')

            subtitle_object = {
                'number': number,
                'start_time': start_time,
                'end_time': end_time,
                'text': subtitle_text
            }

            self._subtitle_.append(subtitle_object)

    def make_file(self, file_path, sub_range=None, encoding='utf-8'):
        pass

smi = SMI()
smi.parse('../data/1001.smi')
smi.make_file('asd')
smi.convert_to('vtt').make_file('../data/result.vtt')
smi.convert_to('srt').make_file('../data/result.srt')