PySubtitle
=============
A simple python tool that helps slice, convert, and shift subtitle file


Useage
=============
Read SRT subtitle file
```
from subtitle.SRT import SRT

srt = SRT()
srt.parse('file_path')
```

Shift and slice subtitle
```
#   5000 milliseconds, 10000 milliseconds
srt.shift(5000).slice(0, 10000)
```

Convert to VTT subtitle and make subtitle file
```
srt.convert_to('VTT').make_file('file_path')
```


Supported types of subtitle
=============
SRT

VTT

SMI (read only)
