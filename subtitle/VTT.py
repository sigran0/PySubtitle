
from subtitle.Subtitle import Subtitle
from utils.string_parser import parse_time_string
from utils.string_parser import lines_to_string
from utils.string_parser import get_hmsms


class VTT(Subtitle):

    def __init__(self, _sub_=None):
        Subtitle.__init__(self, _sub_=_sub_)

    def _read_file(self, file_path, encoding='utf-8', lang='ENCC'):
        with open(file_path, 'r', encoding=encoding) as f:
            lines = f.readlines()
        return lines

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

        if sub_range is None:
            target_list = self._subtitle_
        else:
            target_list = self._get_sub_subtitle_list_(sub_range[0], sub_range[1])

        with open(file_path, 'w') as f:

            f.write('WEBVTT\n')

            for sub in target_list:
                start_time_string = get_hmsms(sub['start_time'], _format='{}:{}:{}.{}')
                end_time_string = get_hmsms(sub['end_time'], _format='{}:{}:{}.{}')

                f.write(str(sub['number']) + '\n')
                f.write('{} --> {}\n'.format(start_time_string, end_time_string))
                f.write(sub['text'] + '\n\n')