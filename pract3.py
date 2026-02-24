class Employee:
    company = "ABC"
    def getdata(self,name,sal,dept):
        self.name=name
        self.sal=sal
        self.dept=dept
emp1=Employee()
emp1.getdata("abc",25000,"developer")
print(emp1.name,emp1.sal,emp1.dept,emp1.company)

emp2=Employee()
emp2.getdata("pqr",45000,"tester")
print(emp2.name,emp2.sal,emp2.dept,emp1.company)

