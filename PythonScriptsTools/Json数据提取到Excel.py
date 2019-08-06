#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Author: lsy
# @Date&Time: 2019/8/6 11:16
# @Description: 把 Json 数据提取到 Excel 表中

import os
import math
import json
import xlwt

path = "C:/Users/qwe/Desktop/"
jsonFilesPath = path + "word search"
excelPath = path + "竞品关卡数据提取.xls"

# 创建 excel
workbook = xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet('Sheet1')

# 所有 json 文件
jsonFiles = [
    os.path.join(jsonFilesPath, jsonFile) for jsonFile in os.listdir(jsonFilesPath)
    if os.path.isfile(os.path.join(jsonFilesPath, jsonFile)) and os.path.splitext(jsonFile)[1] == ".json"
]
# 按文件名特点排序，lambda 返回一个 list，会按数组元素依次比较
jsonFiles.sort(key=lambda x: list(map(int, os.path.split(x)[1].split(".")[0].split("_"))))

# 设置单元格宽度
pixWidth = 2962 // 81 + 1
worksheet.col(1).width = 512 * pixWidth
worksheet.col(3).width = 256 * pixWidth
worksheet.col(4).width = 128 * pixWidth

# 写 excel 文件头
worksheet.write(0, 0, "序号")
worksheet.write(0, 1, "word infos")
worksheet.write(0, 2, "number")
worksheet.write(0, 3, "reward")
worksheet.write(0, 4, "challenge")

# 逐个写入 excel
for i in range(len(jsonFiles)):
    with open(jsonFiles[i], "r", encoding="utf-8") as f:
        row = json.load(f)

        n = i + 1
        wordInfos = ", ".join(row["wordInfos"])
        size = int(math.sqrt(len(row["letterMatrix"])))
        reward = ", ".join(row["reward"])
        challenge = ", ".join(row["challenge"])

        # 序号
        worksheet.write(i + 1, 0, n)
        # word infos
        worksheet.write(i + 1, 1, wordInfos)
        # 行列数
        worksheet.write(i + 1, 2, size)
        # reward
        worksheet.write(i + 1, 3, reward)
        # challenge
        worksheet.write(i + 1, 4, challenge)

        # 打印 log
        print(i + 1)
        print(wordInfos)
        print(size)
        print(reward)
        print(challenge)
        print("--------------------")
        print()
print("complete!")

# 保存
workbook.save(excelPath)
