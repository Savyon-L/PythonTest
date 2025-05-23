"""
单字符匹配：
.    匹配任意单个字符(除了\n)，\.匹配.本身
[]   匹配字符串中的任意单个字符，[^] 匹配不在字符集中的任意单个字符
     []中可以写][a-zA-Z0-9]这三种范围组合或指定单个字符如[aceDFG1351]
\d   匹配数字，即0-9
\D   匹配非数字字符
\s    匹配空白字符，包括空格、制表符、tab、换页符等
\S    匹配非空白字符
\w    匹配字母、数字和下划线，即a-z、A-Z、0-9、_
\W   匹配非单词字符
"""
import re
#
# s = "it1 @@python2 !!666 ##itcast3"
#
# result = re.findall(r'\W',s)#字符串前面带r表示原生字符串，使字符串中的转义字符不生效。
# print(result)
#
# result1 = re.findall(r'[a-zA-Z]', s)#匹配字母
# print(result1)

"""数量匹配：
*      匹配前一个规则的字符0次至无数次
+      匹配前一个规则的字符1次至无数次
?      匹配前一个规则的字符0次或1次
{m}    匹配前一个规则的字符出现m次
{m,}   匹配前一个规则的字符出现m次至无数次
{m,n}  匹配前一个规则的字符出现m次至n次
"""

""""边界的匹配：
^      匹配字符串的开头
$      匹配字符串的结尾
\b     匹配单词的边界
\B     匹配非单词的边界
"""

"""分组匹配：
|   匹配|两边的任意一个表达式
()  将表达式分组，分组内的表达式可以使用\1、\2等引用
"""


#匹配账号，只能由字母和数字组成，长度限制6到10位
# r = '^[0-9a-zA-Z]{6,10}$'
# s = '1234567'
# print(re.findall(r,s))
#匹配QQ号，要求纯数字，长度5到11位，第一位不为0
# r = '^[1-9][0-9]{4,10}$'#加上^$表示匹配整个字符串
# s = '01232434'
# print(re.findall(r,s))
#匹配邮箱地址，只允许QQ、163、Gmail这三种邮箱地址
#{}.{}.{}@{}.{}.{}
r = '(^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$)'
s = 'a.b.c.d.e.f.g@163.com.a.z.c.d.e'
print(re.match(r,s))
print(re.findall(r,s))