#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Author: lsy
# @Date&Time: 2019/8/23 10:26
# @Description: 合并两个词典

import xlrd

excel = xlrd.open_workbook("8-9字词.xlsx")
sheet = excel.sheets()[0]
with open("words_list_filter.txt", 'r', encoding='utf-8') as f:
    txt = f.readlines()
row_sheet = 1
row_txt = 0
word_list_merge = open("word_list_merge.txt", "w", encoding="utf-8")
word_list_merge.write("")

while row_sheet < sheet.nrows and row_txt < len(txt):
    word_sheet = sheet.cell_value(row_sheet, 0)
    word_txt = txt[row_txt]

    if word_sheet < word_txt:
        word_list_merge.write(word_sheet + "\n")
        print(word_sheet)
        row_sheet += 1
    else:
        word_list_merge.write(word_txt)
        print(word_txt, end="")
        row_txt += 1
while row_sheet < sheet.nrows:
    word_list_merge.write(sheet.cell_value(row_sheet, 0) + "\n")
    print(sheet.cell_value(row_sheet, 0))
    row_sheet += 1
while row_txt < len(txt):
    word_list_merge.write(txt[row_txt])
    print(txt[row_txt], end="")
    row_txt += 1

word_list_merge.close()