#继承语法：class 类名（父类名）：
#               类体

"""
#1、单继承
class Phone:
    IMEI = None
    producer = "Apple"

    def call_by_4g(self):
        print("4g通话")

class PhoneX(Phone):
    face_id = "10001"

    def call_by_5g(self):
        print("2022年新功能：5g通话")

phone = PhoneX()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()

#2、多继承:若父类有同名属性或方法，子类会优先使用第一个父类的属性或方法（从左到右）
class NFCReader:
    nfc_type = "第五代"
    producer = "hw"

    def read_card(self):
        print("读取卡片")

    def write_card(self):
            print("NFC写卡片")

class RemoteControl:
    rc_type = "红外线"
    producer = "小米"

    def control_tv(self):
        print("控制电视")

class MyPhone(Phone, NFCReader, RemoteControl):
    pass#pass是一个占位符表示什么都不做，当需要一个语法上合法的代码块但又不想在其中添加任何代码时，可以使用pass语句。

phone = MyPhone()
phone.call_by_4g()
phone.read_card()
print(phone.producer)


#3、复写父类成员
class Phone:
    IMEI = None
    producer = "Apple"

    def call_by_4g(self):
        print("4g通话")

class MyPhone(Phone):
    IMEI = "123456789012345"
    producer = "小米"

    def call_by_4g(self):
        print("5g通话")

phone = MyPhone()
print(phone.producer)
"""

#4、调用父类同名成员:在复写完父类成员后，子类可以通过super()函数或父类名调用父类的同名成员
class Phone:
    IMEI = None
    producer = "Apple"

    def call_by_5g(self):
        print("5g通话")

class MyPhone(Phone):
    producer = "小米"

    def call_by_5g(self):
        print("开启CPU单核模式，确保通话时省电")

        """
        #方式一:使用父类名调用父类同名成员
        print(f"父类的厂商是：{Phone.producer}")
        Phone.call_by_5g(self)
        """
        #方式二:使用super()函数在子类调用父类同名成员
        print(f"父类的厂商是：{super().producer}")
        super().call_by_5g()
        print("关闭CPU单核模式，恢复正常模式")

phone = MyPhone()
phone.call_by_5g()
