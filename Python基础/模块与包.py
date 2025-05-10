#模块导入语法：[from 模块名] import[模块、类、函数名、*（全部导入）] [as 别名]
"""常用格式有：
import 模块名1，模块名2...
from 模块名 import 类、变量、方法等
from 模块名 import *
import 模块名 as 别名
from 模块名 import 类、变量。方法等 as 别名
"""

"""
import time#可以鼠标停在模块名上按ctrl查看time.py模块的文档
time.sleep(1)

from time import sleep#从time模块导入sleep函数
sleep(1)

from time import *
sleep(1)

import time as t#导入time模块并起别名t
t.sleep(1)#使用别名调用模块中的函数

from time import sleep as s#导入time模块中的sleep函数并起别名s
s(1)
"""

"""
#__main__变量，当模块被直接运行时，__name__的值为__main__；当模块被导入时，__name__的值为模块名
from function import test_module
test_module(15,2)
"""

"""
from function import * #这里的*对应__all__中的内容，如果不写__all__，则会导入所有函数
test_module(1,2)
test_module2(1,2)
"""

"""#自定义模块1
import my_package.my_module1
import my_package.my_module2
my_package.my_module1.info_print1()
my_package.my_module2.info_print2()
"""
""""#自定义模块2
from my_package import my_module1
from my_package import my_module2
my_module1.info_print1()
my_module2.info_print2()
"""
"""
#自定义模块3
from my_package import *
my_module1.info_print1()
my_module2.info_print2()
"""
import my_utils.str_util
from my_utils import file_util
a=my_utils.str_util.str_reverse('hello')
b=my_utils.str_util.substr('hello',1,3)
print(a,b)

file_util.print_file_info()