import math


class Student:
    def __init__(self,name,age,clg):
        self.name=name
        self.age=age
        self.clg=clg

    def printinfo(self):
        print(self.name,self.age,self.clg,"are the info of the s1")
s1=Student("James",23,"james")
s1.printinfo()


class Laptop:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def applyDiscount(self):
        if self.price>=80000:
            print("15% discount")
        elif self.price>=50000:
            print("10% discount")
        else:
            print("5% discount")

    def showDetails(self):
        print(self.brand,self.price)

lap=Laptop("mac",110000)
lap.applyDiscount()
lap.showDetails()

class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        area=math.pi*self.radius**2
        print(area)
    def circumference(self):
        circumference=2*math.pi*self.radius
        print(circumference)
c = Circle(7)
c.area()
c.circumference()

class Atm:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def withdraw(self,amount):
        self.balance-=amount
        print(self.name,self.balance)
    def deposit(self,amount):
        self.balance+=amount
        print(self.name,self.balance)
    def checkBalance(self):
        print(self.name,self.balance)
atm=Atm("abc",25000)
atm.withdraw(100)
atm.deposit(100)
atm.checkBalance()




