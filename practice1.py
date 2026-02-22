class Student:
    def setData(self, name , marks):
        self.name=name
        self.marks=marks
    def showGrade(self):
        if self.marks>=40:
            print("A")
        else:
            print("fail")

s=Student()
s.setData("indu",75)
s.showGrade()


class Employee:
    def setDAta(self,name,salary):
        self.name=name
        self.salary=salary

    def showBonus(self):
        if self.salary>=50000:
           print("bonus=10%")
        else:
            print("bonus=5%")

emp=Employee()
emp.setDAta("indu",100000)
emp.showBonus()

class Car:
    def setData(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def show(self):
        print(self.brand)
        print(self.speed)

car=Car()
car.setData("bmw",1000)
car.show()

class Student:
    def setData(self,name,marks):
        self.name=name
        self.marks=marks
    def result(self):
        if self.marks>=40:
            print("A")
        else:
            print("fail")
stud=Student()
stud.setData("indu",100)
stud.result()

class BankAccount:
    def Data(self,name,balance):
        self.name = name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount > self.balance:
            print("cant withdraw")
        else:
            self.balance -= amount
    def showBalance(self):
        print(self.balance)

BA=BankAccount()
BA.Data("indu",20000)
BA.withdraw(1000)
BA.showBalance()

