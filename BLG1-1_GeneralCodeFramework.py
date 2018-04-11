# -*- coding: utf-8 -*-

# 爬虫通用代码框架
import requests
def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status() # 若状态不是200，则引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if __name__ == "__main__":
    url = "http://www.baidu.com"
    print(getHTMLText(url))