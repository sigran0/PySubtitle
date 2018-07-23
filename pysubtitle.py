
import os
import argparse

def process(file_path, target_path, milsec, convert_to, slice_from, slice_to):

    if not os.path.isfile(file_path):
        raise FileNotFoundError()

    if '.smi' in file_path or '.SMI' in file_path:
        file_type = 'smi'
    elif '.srt' in file_path or '.SRT' in file_path:
        file_type = 'srt'
    elif '.vtt' in file_path or '.VTT' in file_path:
        file_type = 'vtt'
    else:
        raise TypeError('this file does not support in this script')



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_file', dest='input_file', required=True, help='Path of the subtitle file to modify')
    parser.add_argument('-o', '--output_file', dest='output_file', required=True, help='Path of the output subtitle fild')
    parser.add_argument('-s', '--shift', dest='milsec', required=False, type=int, help='Count of milliseconds to shift the subtitle\'s delay')
    parser.add_argument('-c', '--convert_to', dest='convert_to', required=False, help='Convert subtitle file')
    parser.add_argument('-z', '--slice_from', dest='slice_from', required=False, help='Slice subtitle file')
    parser.add_argument('-x', '--slice_to', dest='slice_to', required=False, help='Slice subtitle file')

    args = parser.parse_args()