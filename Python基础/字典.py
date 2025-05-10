#字典也使用{}，不过储存元素是一个个的键值对,不重复没有下标索引且无序
dict1={}
dict2=dict()#定义空字典两种方法
dict3={"小明":99,"小红":100,"小黑":12}#定义字典
print(dict3["小明"])#访问字典元素
#字典嵌套
dict4={
    "小马":{
        "语文":99,
        "数学":100
    },"小白":{
        "语文":98,
        "数学":99
    },"小黄":{
        "语文":97,
        "数学":98
    }
}
print(dict4["小马"]["数学"])#访问字典元素

#·字典的新增与更新
my_dict={"小明":99,"小红":100,"小黑":12}
my_dict["小白"]=98#新增
my_dict["小明"]=100#更新
print(my_dict)

#字典的删除
my_dict={"小明":99,"小红":100,"小黑":12}
my_dict.pop("小明")#删除指定元素
print(my_dict)

#字典的清空
my_dict={"小明":99,"小红":100,"小黑":12}
my_dict.clear()#清空字典
print(my_dict)

#获取字典的所有key的方法：keys()
my_dict={"小明":99,"小红":100,"小黑":12}
keys=my_dict.keys()
print(keys)#获取字典的所有key

#字典的遍历方法一：
my_dict={"小明":99,"小红":100,"小黑":12}
keys=my_dict.keys()
for i in keys:
    print(my_dict[i])
#字典的遍历方法二：直接遍历
my_dict={"小明":99,"小红":100,"小黑":12}
for key in my_dict:
    print(my_dict[key])


my_dict1={
    "王力宏":{
        "部门":"科技部",
        "工资":3000,
        "级别":1
    },"周杰伦":{
        "部门":"市场部",
        "工资":5000,
        "级别":2
    },"林俊杰":{
        "部门":"市场部",
        "工资":7000,
        "级别":3
    },"张学友":{
        "部门":"科技部",
        "工资":4000,
        "级别":1
    },"刘德华":{
        "部门":"市场部",
        "工资":6000,
        "级别":2
    },
}
print(f"全体员工当前信息如下:\n{my_dict1}")
for key in my_dict1:
    if my_dict1[key]["级别"]==1:
        my_dict1[key]["级别"]+=1
        my_dict1[key]["工资"]+=1000
print(my_dict1)


#max()函数和min()函数
my_dict={"小明":99,"小红":100,"小黑":12}
my_list=[1,2,3,6,5,1,8,3,4,5]
my_set={1,7,3,2,5}
my_tuple=(1,2,7,3,5)
my_str="hello"
print(max(my_dict))
print(max(my_list))
print(max(my_set))
print(max(my_tuple))
print(max(my_str))
#正向排序,排序结果放入列表
print(sorted(my_list))
print(sorted(my_set))
print(sorted(my_tuple))
print(sorted(my_str))
print(sorted(my_dict))
#反向排序
print(sorted(my_list,reverse=True))
print(sorted(my_set,reverse=True))
print(sorted(my_tuple,reverse=True))
print(sorted(my_str,reverse=True))
print(sorted(my_dict,reverse=True))