# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def display(self):
#         print("hi your name is ",self.name)
#         print("hi your salary is ",self.salary)
#
# class Test:
#     def modify(emp):
#         emp.salary=emp.salary+300000
#         emp.display()
#
# emp=Employee("ABC",10000)
# Test.modify(emp)
#

class Person:

    def __init__(self):
        self.name = "asd"
        self.db = self.dob()

    class dob:

        def __init__(self):
            self.day = 7
            self.month = 4
            self.year = 1988

        def display(self):
            print(self.day, self.month, self.year)


p = Person()
p.db.display()