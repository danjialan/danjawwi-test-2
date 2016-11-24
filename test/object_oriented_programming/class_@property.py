class Student():
    def see_age(self):
        print(self.age)

    def set_age(self,age):
        if not isinstance(age,int):
            print('not int')
        elif age>100 or age<0:
            print('range not right')
        else:
            self.age=age

dan=Student()
dan.set_age(5)
dan.see_age()

class Walun():
    @property
    def see_age(self):
        print(self.age)

    @see_age.setter
    def set_age(self,value):
        if not isinstance(value,int):
            print('not int')
        elif value>100 or value<0:
            print('range not right')
        else:
            self.age=value

jialan = Walun()
jialan.age = 6
jialan.see_age