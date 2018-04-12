# -*-coding=utf-8-*-
import requests
import re
from bs4 import BeautifulSoup # 从bs4库里导入BeautifulSoup类 #import bs4

url = "https://python123.io/ws/demo.html"
r = requests.get(url)
demo = r.text
Soup = BeautifulSoup(demo,"html.parser") # bs4的HTML解析器
print(Soup.prettify()) # prettify()函数，使代码格式显示得标准一些，最后加一个换行符
print(Soup.a) # 第一个a标签信息
print(Soup.a.prettify()) # prettify()会在最后加一个换行符
print(Soup.title)
print(Soup.a.name) # a
print(Soup.a.parent.name) # p
tag = Soup.a
print(tag.attrs) # 返回一个字典：{'href': 'http://www.icourse163.org/course/BIT-268001', 'class': ['py1'], 'id': 'link1'}
print(type(tag.attrs)) # <class 'dict'>
print(tag.attrs['class']) # ['py1']
print(tag.attrs['href']) # http://www.icourse163.org/course/BIT-268001
print(type(tag)) # <class 'bs4.element.Tag'>
print(Soup.a.string) # 第一个a标签的，Basic Python
print(Soup.p.string) # The demo python introduces several python courses.
print(type(Soup.p.string)) # <class 'bs4.element.NavigableString'>

NewSoup = BeautifulSoup("<b><!--This is s comment--></b><p>This is not a comment</p>","html.parser")
print(NewSoup.b.string) # This is s comment
print(type(NewSoup.b.string)) # <class 'bs4.element.Comment'>
print(NewSoup.p.string) # This is not a comment
print(type(NewSoup.p.string)) # <class 'bs4.element.NavigableString'>

# 下行遍历（contents列表类型；children下层儿子节点/decendants所有子孙节点，迭代类型，只能用在for循环语句）
print()
print(Soup.head) # <head><title>This is a python demo page</title></head>
print(Soup.head.contents) # [<title>This is a python demo page</title>]
print(Soup.body.contents) # 包含换行符'\n'
print(len(Soup.body.contents)) # 5
print(Soup.body.contents[1]) # <p class="title"><b>The demo python introduces several python courses.</b></p>

# 上行遍历（parent上层父亲节点，parents所有先辈节点，迭代类型）
print()
print(Soup.title.parent) # <head><title>This is a python demo page</title></head>
print(Soup.html.parent) # 本身

# 平行遍历（平行遍历发生在同一个父节点下的各节点间）（next_sibling/previous_sibling、next_siblings/previous_siblings迭代类型，只能用在for/in结构）
print()
print(Soup.a.next_sibling) # and，即有可能是<></>之间的navigablestring
print(Soup.a.next_sibling.next_sibling) # <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>
print(Soup.a.previous_sibling)
print(Soup.a.previous_sibling.previous_sibling) # None
print(Soup.a.parent) # p标签信息

print()
for link in Soup.find_all('a'):
    print(link.get('href'))

print()
print(Soup('a')) # 查找a标签
print(Soup.find_all(['a','b'])) # 查找a和b标签
print(Soup(['a','b'])) # 与上行等价
# soup()等价于soup.find_all()
# <tag>()等价于<tag>.find_all()

print()
for tag in Soup.find_all(True): # True打印所有标签
    print(tag.name)

print()
for tag in Soup.find_all(re.compile('b')): # 查找包含‘b’的标签
    print(tag.name) # body、b

print()
print(Soup.find_all('p','course')) # 包含属性为course的p标签
print(Soup.find_all(id = 'link1')) # [<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>]
print(Soup.find_all(id = re.compile('link'))) # [<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>, <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>]

print()
print(Soup.find_all('a')) # 从所有子孙节点查找
print(Soup.find_all('a', recursive= False)) # 是否对子孙全部检索，默认True

print()
print(Soup.find_all(string = re.compile('python'))) # ['This is a python demo page', 'The demo python introduces several python courses.']
