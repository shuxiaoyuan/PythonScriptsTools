#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@Author: lishuyuan
@Date&Time: 2019年3月7日 下午1:50:02
@Description: 给定一个单词列表和 Excel 单词翻译列表，输出这个单词列表带翻译的文本文件
'''

import xlrd

excel = xlrd.open_workbook("单词短语翻译列表.xlsx")
sheet = excel.sheets()[0]
row = 1
uncommon_words_with_translations = open("uncommon_words_with_translations.txt", "w", encoding="utf-8")

with open("uncommon_words.txt", 'r', encoding='utf-8') as f:
    for line in f.readlines():
        
        while row < sheet.nrows - 1 and str(sheet.cell_value(row, 0)).strip() < str(line).strip():
            row += 1

        if str(sheet.cell_value(row, 0)).strip() == str(line).strip():
            print("%-10s%s" % (str(sheet.cell_value(row, 0)).strip(), str(sheet.cell_value(row, 1)).strip()))
            print("%-10s%s" % (str(sheet.cell_value(row, 0)).strip(), str(sheet.cell_value(row, 1)).strip()), file=uncommon_words_with_translations)
        elif str(sheet.cell_value(row, 0)).strip() > str(line).strip():
            print(str(line).strip())
            print(str(line).strip(), file=uncommon_words_with_translations)            
        else:
            print("excel 不够全，未完成所有翻译！")
            print("excel 不够全，未完成所有翻译！", file=uncommon_words_with_translations)
            break

uncommon_words_with_translations.close()

