class Animals(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def run(self):
        print('animal is running ')

class Dog(Animals):
    def run(self):
        print('the dog is running')

class Cat(Animals):
    def run(self):
        print('the cat is running')

dog1993 = Dog('dog1993','55')
cat1550 = Cat('cat1993','55')

dog1993.name='561'
cat1550.name='15'

dog1993.run()
cat1550.run()

print(type(dog1993))
print(type(Dog))


