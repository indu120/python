class BankAccount():
    def Accholder(self,holder,balance):
        self.holder=holder
        self.balance=balance

    def deposit(self,amount):
        self.balance +=amount
        print("deposit ",amount)

    def withdraw(self,amount):
            self.balance -=amount
            print("withdraw ",amount)

    def dis(self):
        print("dis ",self.balance)

b=BankAccount()
b.Accholder("xyz",1000)
b.deposit(100)
b.withdraw(100)
b.dis()