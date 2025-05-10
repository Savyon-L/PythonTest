#类型注解只是一个备注不会影响程序运行。语法1、变量：类型
import json
import random

#基础数据变量注解：
var_1: int = 10
var_2: str = "hello"
var_3: bool = True
var_4: float = 3.14
#类对象类型注解：
class Student:
    pass
stu: Student = Student()
#基础容器类型注解：
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_dict: dict = {"key": "value"}
#容器类型详细注解：
new_my_list: list[int] = [1, 2, 3]
new_my_tuple: tuple[int, str,bool]= (1, "帅哥", True)
new_my_dict: dict[str,int] = {"key": 100}


#语法2、在注释中进行类型注解
var_5 = random.randint(1,10)  # type: int
var_6 = json.loads("{'小马':99}")  # type: dict[str,int]
def func():
    return 10
var_7 = func()   #type: int