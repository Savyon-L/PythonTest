import re

s = "1python itheima python itcast python"
#match()方法,从头匹配
result = re.match("python", s)
print(result)
# print(result.span())
# print(result.group())

#search()方法,从头匹配找到就停止，没有就返回None
result = re.search("python", s)
print(result)
print(result.span())
print(result.group())

#findall()方法,返回所有匹配的结果存入列表，没有就返回空列表
result = re.findall("python", s)
print(result)



