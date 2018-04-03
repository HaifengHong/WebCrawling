# -*- coding: utf-8 -*-
import scrapy

# 目标是将http://python123.io/ws/demo.html的整个页面内容保存在本地

class DemoSpider(scrapy.Spider): # 继承自scrapy.Spider
    name = 'demo'
    # allowed_domains = ['python123.io'] # 其实并不需要
    start_urls = ['http://python123.io/ws/demo.html'] # 爬虫启动时最开始的url链接

    def parse(self, response): # response相当于从网络中返回内容所存储的或对应的对象
        fname = response.url.split('/')[-1] # 把response中的内容写到html文件中，定义文件名。从响应的url中提取文件名字作为保存在本地的文件名,即demo.html
        with open(fname, 'wb') as f:
            f.write(response.body) # 将返回的内容保存为文件
        self.log('Saved file %s.' % fname)
