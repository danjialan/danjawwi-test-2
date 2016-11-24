class Student():
    pass

dan = Student()

def add_name(self,name):
    self.name = name

from types import MethodType

dan.add_name = MethodType(add_name,dan)
#不加括号是引用，加括号是使用

dan.add_name('11')
print(dan.name)
#等于说PC有一个bug，就是给实例添加func的时候他没法识别。

Student.add_name = add_name

weilun=Student()
weilun.add_name('22')
print(weilun.name)