"""#集合不支持重复元素且无序,所以不支持下标访问，允许修改
my_set={"我是帅哥","四川成都","黑马程序员","我是帅哥","四川成都","黑马程序员"}
my_set_empty=set()#定义空集合
print(my_set)
#集合的添加
my_set.add("hello")
#集合的删除
my_set.remove("hello")#删除指定元素
my_set.discard("hello")#删除指定元素，不存在时不报错
print(my_set)
#集合随机取出元素pop()
element=my_set.pop()#随机删除一个元素
print(element,my_set)
#集合的清空
my_set.clear()#清空集合
print(my_set)
#取两个集合的差集
my_set1={"hello","world","python"}
my_set2={"hello","java","c++"}
my_set3=my_set1.difference(my_set2)#取集合一中集合二没有的元素
print(my_set3)
#消除交集
my_set1={"hello","world","python"}
my_set2={"hello","java","c++"}
my_set1.difference_update(my_set2)#取集合一中集合二没有的元素赋值给集合一，集合二不变
print(my_set1)
print(my_set2)
#集合的合并
my_set1={"hello","world","python",1,}
my_set2={"hello","java","c++"}
my_set3=my_set1.union(my_set2)#合并两个集合
print(my_set3)
#集合的遍历，不支持while支持for
for item in my_set1:
    print(item)
"""


my_list=[1,2,3,4,5,1,2,3,4,5]
my_set_empty=set()
for item in my_list:
    my_set_empty.add(item)
print(my_set_empty)


