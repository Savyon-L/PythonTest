#json转换网址：ab123
#json是一种中转数据格式(字符串格式)，相当于python的列表或字典
import json
data=[{"name":"张大山","age":11},{"name":"王大锤","age":13},{"name":"赵小虎","age":16}]
#json.dumps()将python字典转换为json字符串
josn_str=json.dumps(data,ensure_ascii=False)#ensure_ascii=False表示中文字符不转义
print(josn_str)

#json.loads()将json字符串数据转换为python字典或列表
s='[{"name": "张大山", "age": 11}, {"name": "王大锤", "age": 13}, {"name": "赵小虎", "age": 16}]'
sl=json.loads(s)
print(sl)

