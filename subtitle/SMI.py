
from subtitle.Subtitle import Subtitle
from samitizer import Smi
from utils.string_parser import parse_time_string
from utils.string_parser import lines_to_string


class SMI(Subtitle):

    def __init__(self):
        Subtitle.__init__(self)

    def _read_file(self, file_path, encoding='utf-8'):
        smi = Smi(file_path)
        return smi.convert('vtt', lang='ENCC')

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

            self._subtitle.append(subtitle_object)

    def make_file(self, file_path, encoding='utf-8'):
        pass