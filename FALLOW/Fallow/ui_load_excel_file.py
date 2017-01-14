import sys
from PyQt4 import QtGui
import xlrd as wb

book = wb.open_workbook('sample.xls')
sheet = book.sheet_by_name('Sheet1')
# sheet.col_values


# print keys
keys = sheet.col_values(0, 0, 4)
d = {}
d[keys[0]] = {}
for col in range(0, 5):
    keys = sheet.col_values(col, 0, 4)
    pre_value = d
    for i, key in enumerate(keys[1:]):
        next_value = pre_value[keys[i]]
        if key and key not in next_value:
            if i == len(keys)-2 or keys[i+2] == '':
                next_value[key] = 'a'
                break
            next_value[key] = {}
        pre_value = next_value


# print s['harverst']

import json
print json.dumps(d, indent=2)
    # print d
    # print key, keys[i]


# read_table(sheet, 0, 4, 0, 3, 10)
# print d
