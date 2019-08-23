#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
@Author: lishuyuan
@Date&Time: 2018年11月20日 下午4:06:14
@Description: 将原词典 文本文件中长度为 3~7 的单词输出到一个新的文本文件中
'''

with open("words.txt", "w", encoding="utf-8") as f:
    f.write("")
words = open("words.txt", 'w', encoding='utf-8')
with open("wordslistexport.txt", "r", encoding='utf-8') as f:
    for line in f.readlines():
        if len(line.strip()) == 8 or len(line.strip()) == 9:
            words.write(line)
words.close()