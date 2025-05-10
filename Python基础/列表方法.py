"""#1.负索引
name_list=["小明","小红","小刚"]
print(name_list[-1])
#2.嵌套列表查询
name_list=[["小明","小红","小刚"],["小白","小黑","小黄"]]
print(name_list[0][1])
#3.index()方法查询元素下标
name_list=["小明","小红","小刚"]
index=name_list.index("小红")
print(index)
#4.修改列表元素
name_list=["小明","小红","小刚"]
name_list[1]="小白"
print(name_list)
#5.插入元素,在指定下标插入
name_list=["小明","小红","小刚"]
name_list.insert(1,"小白")
print(name_list)
#6.追加元素，将元素添加到列表末尾
name_list= ["小明", "小红", "小刚", "小白"]
name_list.append("ef")
print(name_list)
#7.扩展列表，将一个列表的元素添加到另一个列表末尾
name_list1=["小明","小红","小刚"]
name_list2=["小白","小黑","小黄"]
name_list2.extend(name_list1)
print(name_list2)
#8.删除列表元素
name_list=["小明","小红","小刚"]
del name_list[1]
print(name_list)
#9.pop()方法删除列表元素,这个值可以被接收
name_list=["小明","小红","小刚"]
element=name_list.pop(1)
print(element)
#10.remove()方法删除指定元素,从左边开始删除
name_list=[1,2,3,4,7,4,6,7,9]
name_list.remove(4)
print(name_list)
#11.clear()方法清空列表
name_list=[1,2,3,4,5]
name_list.clear()
print(name_list)
#12.统计某元素在列表里的个数
name_list=[1,2,3,4,1,6,1,8,9,1]
print(name_list.count(1))
#13.统计列表长度
name_list=[1,2,3,4,5]
print(len(name_list))
#14.列表升序排列
name_list=[1,7,3,2,5]
name_list.sort()
print(name_list)
#15.列表降序排列
name_list=[1,7,3,2,5]
name_list.sort(reverse=True)
print(name_list)"""

#列表循环遍历
def list_while_func():
    name_list=["小明","小红","小刚"]
    index=0
    while index<len(name_list):
        print(name_list[index])
        index+=1
list_while_func()

def list_for_func():
    name_list=[1,2,3,4,5,6,7,8,9]
    for index in range(len(name_list)):
        if index%2!=0:
            print(name_list[index])
list_for_func()


"""sort()方法与sorted函数的区别：
1.sort()方法只能用于列表并原地修改列表，而sorted函数可以用于任何可迭代对象，如列表、元组、字符串等，他会返回一个新的列表。
2.sort(key,reverse):sort用两个可选参数key和reverse来指定排序规则，key是一个函数，使用时将列表所有值传入key所用的函数中再由key指定排序时的关键值，reverse是一个布尔值，指定排序顺序。
"""
my_list = [("小明", 18), ("小红", 20), ("小刚", 19)]
# sort()方法,列表中元素全部传入x
my_list.sort(key=lambda x:x[1],reverse=False)
print(my_list)



x=1,2,4,5,6
list(x)
print(x)