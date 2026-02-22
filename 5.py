class Employee:
    def setData(self, name, id , dept):
        self.name= name
        self.id= id
        self.dept= dept

    def display(self):
        print(self.name)
        print(self.id)
        print(self.dept)

e = Employee()
e.setData("indu",100,"asd")
e.display()



# global variable

a = 10
def fun1():
    # here we are creating a local varial a inside the fun1 we are not accessing the global varial
    a=50
    print(a)
fun1()


def fun2():
    # here we are accessing the global variable a using the global keyword
    global a
    print(a)
fun2()