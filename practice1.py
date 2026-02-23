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

class Emp:
    def Data(self , name, basic_salary):
        self.name=name
        self.basic_salary=basic_salary
    def calculateSalary(self):
        if self.basic_salary>=50000:
            print("bonus is 20%of salary")
        elif self.basic_salary>=30000:
            print("bonus is 10% of salary")
        else:
            print("bonus is 5% of salary")

    def finalSalary(self):
        print(self.basic_salary)

emp=Emp()
emp.Data( "indu",100000)
emp.calculateSalary()
emp.finalSalary()

class ShoppingCart:
    def setData(self,name,total_amount):
        self.name=name
        self.total_amount=total_amount

    def  setCustomer(self,name):
        self.name=name
    def addItem(self,price):
        self.total_amount+=price
    def applyDiscount(self):
        if self.total_amount >=5000:
            print("20% discount")
        elif self.total_amount >=2000:
            print("10% discount")
        else:
            print("no discount")


sc =ShoppingCart()
sc.setData("indu",1000)
sc.setCustomer("indu")
sc.addItem(250)
sc.addItem(150)
sc.addItem(550)
sc.addItem(50)
sc.applyDiscount()

class Book:
    def data(self,title,author):
        self.title=title
        self.author=author
    def display(self):
        print(self.title,self.author)

b=Book()
b.data("aa","bbb")
b.display()

class Calci:
    def setData(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        self.sum=self.num1+self.num2
        print(self.sum , "sum of 2 digit")
    def sub(self):
        self.diff=self.num1-self.num2
        print(self.diff , "difference of 2 digit")

cal=Calci()
cal.setData(23,25)
cal.add()
cal.sub()

