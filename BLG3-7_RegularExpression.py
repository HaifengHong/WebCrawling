# -*- coding: utf-8 -*-
import re

# re.search(pattern, string, flags=0))返回match对象
match = re.search(r'[1-9]\d{5}', 'BIT 100081') # raw string原生字符串
if match:
    print(match.group(0)) # 100081

# re.match(pattern, string, flags=0))返回match对象。从字符串起始位置匹配，如果不是起始位置匹配成功，返回none
print()
# match1 = re.match(r'[1-9]\d{5}', 'BIT 100081')
# print(match1.group(0)) # AttributeError: 'NoneType' object has no attribute 'group'。空变量无法调用group方法
match2 = re.match(r'[1-9]\d{5}', '100081 BIT') # 返回match对象。
print(match2.group(0))

# re.findall(pattern, string, flags=0))返回列表
print()
ls = re.findall(r'[1-9]\d{5}', 'BIT100081 TSU100084')
print(ls)

# re.split(pattern, string, maxsplit=0, flags=0)返回列表， maxsplit最大分割数，剩余部分作为最后一个元素输出
print()
ls1 = re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084')
print(ls1) # ['BIT', ' TSU', '']
ls2 = re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084', maxsplit=1)
print(ls2) # ['BIT', ' TSU100084']

# re.finditer(pattern, string, flags=0)返回匹配结果的迭代类型，每个迭代元素是match对象
print()
for m in re.finditer(r'[1-9]\d{5}', 'BIT100081 TSU100084'):
    if m:
        print(m.group(0))

# re.sub(pattern, repl, string, count=0, flags=0)返回替换后的字符串
print()
str = re.sub(r'[1-9]\d{5}', ':zipcode', 'BIT100081 TSU100084')
print(str) # BIT:zipcode TSU:zipcode


########等价用法##########
# 函数式用法：一次性操作
rst = re.search(r'[1‐9]\d{5}', 'BIT 100081')
# 面向对象用法：编译后的多次操作
regex = re.compile(r'[1‐9]\d{5}')
rst = regex.search('BIT 100081')


# RE库的match对象
# match对象的属性
m = re.search(r'[1-9]\d{5}', 'BIT100081 TSU100084')
print(m.string) # BIT 100081 待匹配的文本
print(m.re) # re.compile('[1-9]\\d{5}') 匹配时使用的patter对象（正则表达式）
print(m.pos) # 0 正则表达式搜索文本的开始位置
print(m.endpos) # 19 正则表达式搜索文本的结束位置
# match对象的方法
print(m.group(0)) # 100081 等价于print(m.group())。match对象只包含一次匹配的结果，若要显示所有匹配结果使用finditer()
print(m.start()) # 3 匹配字符串在原始字符串的开始位置
print(m.end()) # 9 匹配字符串在原始字符串的结束位置
print(m.span()) # (3, 9) 返回(.start(), .end())


# RE库默认采用贪婪匹配，输出匹配最长的子串
m1 = re.search(r'PY.*N', 'PYANBNCNDN')
print(m1.group(0))
m2 = re.search(r'PY.*?N', 'PYANBNCNDN') # 最小匹配（最小匹配操作符：*?、+?、??、{m,n}?）
print(m2.group(0))

m1 = re.findall(r"[\d.]*", '1345 193.20 12.0')
print(m1) # ['1345', '', '193.20', '', '12.0', '']