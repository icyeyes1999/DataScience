#@by yst 2020.7.02
#修改只需要修改files，path1，path3根据需要来修改
from __future__ import unicode_literals
import xlrd
from collections import OrderedDict
import json
import codecs
path1 = 'C:/Users/ty/Desktop/抖查查榜单数据/抖查查-抖数据查询平台'
path2 = '.xlsx'
path3 = 'C:/Users/ty/Desktop/抖查查榜单数据/JSON/'
files = [
    '6.16',
    '6.17',
    '6.18',
    '6.19',
    '6.21',
    '6.22',
    '6.23',
    '6.24',
    '6.26',
    '6.27',
    '6.28',
    '6.29',
    '6.30',
    '7.1',
    '7.2',
    '7.3',
    '7.4',
    '7.5'
]
for i in range(len(files)):
    wb = xlrd.open_workbook(path1+files[i]+path2)
    convert_list = []
    sh = wb.sheet_by_index(0)
    title = sh.row_values(0)
    for rownum in range(1, sh.nrows):
        rowvalue = sh.row_values(rownum)
        single = OrderedDict()
        for colnum in range(0, len(rowvalue)):
            print(title[colnum], rowvalue[colnum])
            single[title[colnum]] = rowvalue[colnum]
        #print(single)
        convert_list.append(single)

    j = json.dumps(convert_list,ensure_ascii=False,indent=4)
    with codecs.open(path3+files[i]+'file.json', "w", "utf-8") as f:
        f.write(j)
