#使用Union类型必须先导包
from typing import Union
my_list: list[Union[int,str,float,bool]] = [1,2,"itheima",3.14,True]

def func(data: Union[int,str]) -> Union[int,str]:
    return data

func(1)
