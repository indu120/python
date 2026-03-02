# def fun(*num):
#     print(num)
#
# fun(1,2,3,4)
#
# def fun1(*n):
#     print(sum(n))
# fun1(20,30,40,50)
#
#
#
# def data(**data):
#     print(data)
#
# data(name = "indu",age = 21,gender = "female")


def outer():
    msg = "hi from outer"
    print(msg)
    # print(imsg)
    def inner():
        imsg = "hi from inner"
        print(imsg)

    # inner()

print(outer())
