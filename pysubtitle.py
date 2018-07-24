
import os
import argparse
from subtitle.SMI import SMI
from subtitle.SRT import SRT
from subtitle.VTT import VTT

def process(file_path, target_path, milsec=None, convert_to=None, slice_from=None, slice_to=None, lang='ENCC'):

    if not os.path.isfile(file_path):
        raise FileNotFoundError()

    if '.smi' in file_path or '.SMI' in file_path:
        file_type = 'smi'
        subt = SMI()
    elif '.srt' in file_path or '.SRT' in file_path:
        file_type = 'srt'
        subt = SRT()
    elif '.vtt' in file_path or '.VTT' in file_path:
        file_type = 'vtt'
        subt = VTT()
    else:
        raise TypeError('this file does not support in this script')
    
    subt.parse(target_path)
    
    if slice_from is not None and slice_to is not None:
        subt.slice(slice_from, slice_to)
    
    if milsec is not None:
        subt.shift(milsec)
    
    if convert_to is not None:
        subt.convert_to(convert_to)
    
    subt.make_file(target_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_file', dest='input_file', required=True, help='Path of the subtitle file to modify')
    parser.add_argument('-o', '--output_file', dest='output_file', required=True, help='Path of the output subtitle fild')
    parser.add_argument('-s', '--shift', dest='milsec', required=False, type=int, help='Count of milliseconds to shift the subtitle\'s delay')
    parser.add_argument('-c', '--convert_to', dest='convert_to', required=False, help='Convert subtitle file')
    parser.add_argument('-z', '--slice_from', dest='slice_from', required=False, help='Slice subtitle file')
    parser.add_argument('-x', '--slice_to', dest='slice_to', required=False, help='Slice subtitle file')
    parser.add_argument('-l', '--language', dest='lang', required=False, help='Language setting')

    args = parser.parse_args()
    process(args.input_file, args.output_file, args.milsec, args.convert_to, args.slice_from, args.slice_to, args.lang)
