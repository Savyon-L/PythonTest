#多态：同样的函数，传入不同的对象，得到不同的状态
#多态的好处：可以用同一个函数名来处理不同类型的对象，简化代码
#多态常用在继承关系上，比如函数形参声明接受父类对象，实际传入父类的子类对象进行工作

class Animal:     #含有抽象方法的类称为抽象类
    def speak(self):
        pass#方法体是空实现的（pass）就是抽象方法

class Dog(Animal):
    def speak(self):
        print( "Woof!")

class Cat(Animal):
    def speak(self):
        print( "Meow!")

dog = Dog()
cat = Cat()

def make_noise(animal: Animal):
    animal.speak()

make_noise(dog)
make_noise(cat)


#抽象类:用来做为其他类提供一个公共接口的类，不能被实例化
class AC:
    def cool_wind(self):
        pass
    def hot_wind(self):
        pass
    def swing_l_r(self):
        pass

#抽象类的子类必须实现父类的所有抽象方法，否则子类也会变成抽象类
class MediaAC(AC):
    def cool_wind(self):
        print("美的空调制冷")
    def hot_wind(self):
        print("美的空调制热")
    def swing_l_r(self):
        print("美的空调左右摆风")

class GreeAC(AC):
    def cool_wind(self):
        print("格力空调制冷")
    def hot_wind(self):
        print("格力空调制热")
    def swing_l_r(self):
        print("格力空调左右摆风")

def make_cool(ac: AC):
    ac.cool_wind()
    ac.hot_wind()
    ac.swing_l_r()

media_ac = MediaAC()
gree_ac = GreeAC()

make_cool(media_ac)
make_cool(gree_ac)

