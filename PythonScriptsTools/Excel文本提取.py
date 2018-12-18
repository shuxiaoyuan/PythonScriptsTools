#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@Author: lishuyuan
@Date&Time: 2018年11月20日 下午4:48:34
@Description: 从 Excel 表格中提取文本，然后输出到文本文件中
'''

import xlrd

path = "level.xlsx"
excel = xlrd.open_workbook(path)
sheet = excel.sheets()[0]
levels = open("levels.txt", 'a', encoding='utf-8') 

for i in range(1, sheet.nrows):
    levels.write(
        str(int(sheet.cell_value(i, 0))) + "," +
        str(sheet.cell_value(i, 1)) + "," +
        str(sheet.cell_value(i, 2)) + "," +
        str(sheet.cell_value(i, 3)) + "," +
        str(sheet.cell_value(i, 4)) + "," +
        str(sheet.cell_value(i, 5)) + "\n" 
    )

levels.close()