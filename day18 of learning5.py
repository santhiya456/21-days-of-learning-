class Person:
    def info(self):
        print("Person details")

class Student(Person):
    def study(self):
        print("Student studies")

class Employee(Person):
    def work(self):
        print("Employee works")

class Intern(Student, Employee):
    pass

i = Intern()
i.info()
i.study()
i.work()
