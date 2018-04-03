# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BaidustocksPipeline(object):
    def process_item(self, item, spider):
        return item

class BaidustocksInfoPipeline(object):
    def open_spider(self, spider): # 当一个爬虫被调用时对应的pipeline启动/用的方法
        self.f = open('BaiduStockInfo.txt', 'w')

    def close_spider(self, spider): # 当一个爬虫关闭或结束时pipeline对应的方法
        self.f.close()

    def process_item(self, item, spider): # 对每一个item项进行处理时对应的方法，也是pipeline中最主体的函数
        try:
            line = str(dict(item)) + '\n'
            self.f.write(line)
        except:
            pass
        return item
