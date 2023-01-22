import json
from io import StringIO
str_io_obj = StringIO('["Ukraine", "United Kingdom", "Ukraine", "United States"]')

#load from StringIO

print('Load: ' + str(json.load(str_io_obj)))
print('String to Json: ' + str(json.loads
                ('{"Ukraine" : 100, "United Kingdom" : 102, "Ukraine" : 100, "United States" : 103}')))