#在函数嵌套的前提下，内部函数使用了外部函数的变量，并且外部函数返回了内部函数，这个使用外部函数的变量的内部函数就叫做闭包。
#nonlocal关键字可以在闭包中修改外部函数的变量

def account_create(initial_amount = 0):
    def atm(num,deposit = True):
        nonlocal initial_amount
        if deposit:
            initial_amount += num
            print(f"存款{num}元，账户余额{initial_amount}元")
        else:
            initial_amount -= num
            print(f"取款{num}元，账户余额{initial_amount}元")
    return atm

fn = account_create()
fn(1000)
fn(2000,False)
del fn

