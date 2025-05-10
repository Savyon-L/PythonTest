#对形参注解
def add(x: int,y: int):
    return x + y
add(1,3)

#对返回值注解
def func(data:list) -> list:
    return data
func([1,2,3])
