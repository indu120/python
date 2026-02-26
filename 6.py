class Student:
    clg = "gmit"

    def setData(self,name, age):
        self.name = name
        self.age = age
s1=Student()
s1.setData("aa",19)
print(s1.name,s1.age,s1.clg)
s2=Student()
s2.setData("bb",20)
print(s2.name,s2.age,s2.clg)

s3=Student()
s3.setData("cc",21)
# modifiying static variable
Student.clg= "UBDT"
print(s3.name,s3.age,s3.clg)


