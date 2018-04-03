# -*- coding: utf-8 -*-
import scrapy
import re

class StocksSpider(scrapy.Spider):
    name = 'stocks'
    # allowed_domains = ['baidu.com']
    start_urls = ['http://quote.eastmoney.com/stocklist.html']

    def parse(self, response):
        for href in response.css('a::attr(href)').extract(): # 用CSS Selector提取信息
            try:
                stock = re.findall(r'[s][hz]\d{6}', href)
                url = 'https://gupiao.baidu.com/stock' + stock + '.html' # 百度股票对应的链接
                yield scrapy.Request(url, callback=self.parse_stock) # callback给出处理这个url对应响应的处理函数
            except:
                continue

    def parse_stock(self, response):
        infoDict = {}
        stockInfo = response.css('.stock-bets')
        name = stockInfo.css('.bets-name').extract()[0]
        keyList = stockInfo.css('dt').extract()
        valueList = stockInfo.css('dd').extract()
        for i in range(len(keyList)):
            key = re.findall(r'>.*</dt>', keyList[i][0][1:-5])
            try:
                val = re.findall(r'\d+\.?.*</dd>', valueList[i][0][0:-5])
            except:
                val = '--'
            infoDict[key] = val

        infoDict.update(
            {'股票名称': re.findall('\s.*\(', name)[0].split()[0] + \
                re.findall('\>.*<', name)[0][1:-1]})
        yield infoDict
