# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import traceback
import re

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

def getStockList(lst, stockURL): # lst列表保存的列表类型，存储了所有股票的信息；stockURL获得股票列表的url网站
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r'[s][hz]\d{6}', href)[0]) # 为何加[0]?
        except:
            continue

def getStockInfo(lst, stockURL, fpath):
    count = 0 # 为了增加进度条
    for stock in lst:
        url = stockURL + stock + '.html'
        html = getHTMLText(url)
        try:
            if html == '': # 判断是否为空页面
                continue
            infoDict = {} # 存储当前从一个页面中返回的或记录的所有个股信息
            soup = BeautifulSoup(html, 'html.parser') # 构建解析网页的类型
            stockInfo = soup.find('div', attrs={'class':'stock-bets'}) # find是找第一个div标签。所有股票信息封装在div标签下，它的属性是class="stock-bets",所以可以搜索这个标签，找到股票所存在的大标签信息，定义为stockInfo

            name = stockInfo.find_all(attrs={'class': 'bets-name'})[0] # AttributeError: 'NoneType' object has no attribute 'find_all'
            infoDict.update({'股票名称': name.text.split()[0]}) # 因为某些名称后面还关联了其他标识符，采用空格分开后获得第一部分也就是完整的股票名称，其余部分舍弃。

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val

            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                count += 1
                print('\r当前速度：{:.2f}%'.format(count*100/len(lst)), end='') # 增加不换行的动态显示的进度条
        except:
            count += 1
            print('\r当前速度：{:.2f}%'.format(count*100/len(lst)), end='')
            # traceback.print_exc()
            continue

def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html' # 获得股票列表的链接
    stock_info_url = 'https://gupiao.baidu.com/stock/' # 获得股票信息的链接的主体部分
    output_file = 'D:\PyCharmCommunityEdition2017.2.4\PyTests\WebCrawling_BLG\BaiduStockInfo.txt'
    slist = [] # 股票信息变量
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)

main()

# 出现部分股票爬取数据为空的情况，因此报错AttributeError: 'NoneType' object has no attribute 'find_all'