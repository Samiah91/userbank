class User:

    def __init__(self,name,account_balance=0):
        self.name = name
        self.account_balance = account_balance


    def deposit(self, amount):
        self.account_balance += amount
        print(self.account_balance, end=" ")
        return self

    def make_withdrawl(self, amount):
        self.account_balance -= amount 
        print(self.account_balance, end=" ")
        return self

    def display(self):
        print(self.name,self.account_balance, end=" ")
        return self

S=User('Mark',3000)
M=User('Jill',2000)
N=User('Ramsy',1000)


S.deposit(600).deposit(100).deposit(70).make_withdrawl(50).display()

M.deposit(100).deposit(90).make_withdrawl(300).make_withdrawl(30).display()

N.deposit(300).make_withdrawl(100).make_withdrawl(100).make_withdrawl(100).display()
