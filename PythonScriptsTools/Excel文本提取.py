#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Author: lsy
# @Date&Time: 2019/8/9 10:02
# @Description: 从 Excel 中提取数据生成关卡

import xlrd

path = "level new.xlsx"
excel = xlrd.open_workbook(path)
sheet = excel.sheets()[0]
with open("levels.txt", "w", encoding="utf-8") as f:
    f.write("")
levels = open("levels.txt", 'a', encoding='utf-8')

for i in range(1, 181):
    line = str(int(sheet.cell_value(i, 1))) + ", " + \
            str(int(sheet.cell_value(i, 6))) + ", " + \
            str(int(sheet.cell_value(i, 5)) if str.strip(str(sheet.cell_value(i, 5))) else " ") + ", " + \
            str(sheet.cell_value(i, 2)) + ", " + \
            str(sheet.cell_value(i, 3)) + ", " + \
            str(sheet.cell_value(i, 4)) + "\n"
    levels.write(line)
    print(line)

levels.close()
