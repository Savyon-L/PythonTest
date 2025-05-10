#元组与列表一样都是可以封装多个不同类型的元素在内，但与列表不同的是，元组一旦定义完成就不能被修改。
t1=("hi",1,True)
t2=(1,)#单个元素后面要加逗号
t3=((1,2,3),(4,5,6))#嵌套元组
print(t3[1][2])
#查找元素下标
t4=("hi",1,True,"hello")
print(t4.index(True))
print(t4.count(1))
for item in t4:
    print(item)
#元组里的列表可以修改
t5=(1,2,3,[4,5,6])
t5[3][0]=100
print(t5)


#字符串索引、字符串不能修改
name="hello world"
print(name[-5])
#字符串的替换，不是修改字符串本身而是返回一个新的字符串
name2=name.replace("he","csgo")
print(f"原字符串{name}被改为{name2}")
#字符串的分割，字符串本身不变而是得到一个新的列表
my_str="hello python handsome smart"
my_str_list=my_str.split(" ")
print(my_str_list)
#字符串的规整操作（不传入参数就只去除前后空格、换行符）
my_str="   hello python handsome lip   "
my_str=my_str.strip()
print(my_str)
print(my_str.strip("hp"))#传入参数就分别去除前后h和p
#字符串的拼接
my_str1="hello"
my_str2="world"
my_str3=my_str1+my_str2
print(my_str3)

#序列是一个有序的元素集合，列表、元组、字符串都是序列
#序列的切片
my_list=[1,2,3,4,5,6]
print(my_list[1:4])#步长可以省略
print(my_list[:])#都不写表示从头到尾
print(my_list[::2])#步长为2
print(my_list[::-1])#步长为-1表示反转

my_str="万过薪月，员序程马黑来，nohtyp学"
my_str1=my_str[::-1][9:14]
print(my_str1)

