#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@Author: lishuyuan
@Date&Time: 2019年3月8日 上午11:29:56
@Description: 给定一个单词表，和由此用 notepad++ 插件导出的原始不常用词表，以及根据这个原始不常用词表手动筛出的可以留下的不常用词表，导出筛除不常用词的单词表
'''

import xlrd

# 原始单词表 set，末尾带 \n
words_set = set(open("words_list.txt", "r", encoding="utf-8").readlines())

# 不常用词 set，末尾带 \n
uncommon_words_set = set(open("uncommon_words.txt", "r", encoding='utf-8').readlines())

# 不常用词中挑出留下的词表，末尾带 \n
uncommon_words_filter_set = set(line + "\n" for line in xlrd.open_workbook("uncommon_words_with_translations.xlsx").sheets()[0].col_values(0))

# 最终结果
words_list_filter = sorted(list(words_set - (uncommon_words_set - uncommon_words_filter_set)))

# 导出筛除不常用词的单词表
with open("words_list_filter.txt", 'w', encoding='utf-8') as f:
    for word in words_list_filter:
        f.write(word)
