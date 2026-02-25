class Test:
    count=0
    def __init__(self):
        Test.count=Test.count+1
t1 = Test()
t2=Test()
t3=Test()
print(t1.count,"is the test counts")

class Train:
    count=100
    def __init__(self):
        Train.count=Train.count-1
t1 = Train()
t2=Train()
t3=Train()
print(t1.count,"is the seat counts")
