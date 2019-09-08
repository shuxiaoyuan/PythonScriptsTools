#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Author: lsy
# @Date&Time: 2019/9/8 13:38
# @Description: 爬取 google play 免费游戏区的前 500 名

from time import sleep
from selenium import webdriver
from scrapy import Selector

rank = 500
driver_path = 'C:/Users/shuyu/Desktop/chromedriver_win32/chromedriver.exe'
domain = 'https://play.google.com'
url = domain + '/store/apps/collection/cluster?clp=0g4cChoKFHRvcHNlbGxpbmdfZnJlZV9HQU1FEAcYAw%3D%3D:S:ANO1ljJ_Y5U&gsr=Ch_SDhwKGgoUdG9wc2VsbGluZ19mcmVlX0dBTUUQBxgD:S:ANO1ljL4b8c'

# Chrome 浏览器
driver = webdriver.Chrome(driver_path)
driver.get(url)

while True:

    # 滑动到页面底部
    js = "window.scrollTo(0, document.body.scrollHeight)"
    driver.execute_script(js)

    # 页面加载等待 5 s
    sleep(5)

    # 若出现 SEE MORE 则点击
    see_more = driver.find_elements_by_xpath('//*[@class="PFAhAf"]/div')
    if see_more:
        see_more[0].click()

    # 若网页加载的游戏超过定义的 rank 值，则退出循环
    html = Selector(text=driver.page_source, type='html')
    if(len(html.xpath('//*[@class="vU6FJ p63iDd"]'))) >= rank:
        break

driver.close()

game_names = html.xpath('//*[@class="WsMG1c nnK0zc"]/text()').extract()
game_links = html.xpath('//*[@class="JC71ub"]/@href').extract()
developer_names = html.xpath('//*[@class="mnKHRc"]/div/text()').extract()
developer_links = html.xpath('//*[@class="mnKHRc"]/@href').extract()

for i in range(rank):
    print('Rank: ', i + 1)
    print('Game: ' + game_names[i] + '(' + domain + game_links[i] + ')')
    print('Developer: ' + developer_names[i] + '(' + domain + developer_links[i] + ')')
    print()
