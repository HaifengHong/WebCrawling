# -*- coding: utf-8 -*-
import requests

# 实例1：京东商品页面的爬取
url = "https://item.jd.com/23323267884.html"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败")


# 实例2：亚马逊商品页面的爬取（原始'User-Agent': 'python-requests/2.18.4'）
url = "https://www.amazon.cn/dp/B078FFX8B6/457-5385668-4860529?_encoding=UTF8&_encoding=UTF8&ref_=pc_cxrd_658390051_recTab_658390051_t_1&pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=merchandised-search-4&pf_rd_r=7VXTXG24WN1CRNC2PT9F&pf_rd_r=7VXTXG24WN1CRNC2PT9F&pf_rd_t=101&pf_rd_p=7e00fee6-4e12-48f0-b4af-b99068b52067&pf_rd_p=7e00fee6-4e12-48f0-b4af-b99068b52067&pf_rd_i=658390051"
try:
    kv = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url, headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("爬取失败")
print(r.request.headers) # {'user-agent': 'Mozilla/5.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}

# 实例3：百度/360搜索关键词提交
keyword = 'python'
try:
    kv = {'wd': keyword}
    r = requests.get("http://www.baidu.com/s", params = kv) # s后不需加?
    print(r.request.url) # http://www.baidu.com/s?wd=python
    r.raise_for_status()
    print(len(r.text))
except:
    print("爬取失败")

# 网络图片的爬取和存储
import os
url = "http://image.ngchina.com.cn/2017/0411/20170411122223468.jpg"
root = "D:\PyCharmCommunityEdition2017.2.4\PyTests\WebCrawling_BLG\pics" # 要事先创建好pics文件夹
path = root + '\\' + url.split('/')[-1] # path:D:\PyCharmCommunityEdition2017.2.4\PyTests\WebCrawling_BLG\pics\20170411122223468.jpg
try:
    if not os.path.exists(root):
        os.mkdir(path)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content) # r.content二进制
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print('爬取失败')

# IP地址所属地查询
url = "http://www.ip38.com/ip.php?ip="
IPAdd = url + "112.96.173.225"
try:
    r = requests.get(IPAdd)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
    print("爬取失败")