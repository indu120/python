def fun1(name,age):
    print(name,age)

fun1("indu",21)

def fun2(name,age):
    print(name,age)

fun2(age=21,name="indu")


def getData(name = None ,age = None,marks=None ):
    if name != None and age!=None and marks != None:
        print("your name",name)
        print("your age",age)
        print("your marks",marks)
    elif name != None and age != None:
        print("your name",name)
        print("your age",age)
    elif marks != None:
        print("your name",name)
    else:
        print("invalid")

getData(name="indu",age=21,marks=10)