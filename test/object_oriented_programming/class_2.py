class Student(object):
    name = 'i am a student'

dan = Student()

dan.name='i am dan'
print(dan.name)
print(Student.name)
del dan.name
print(dan.name)
print(Student.name)