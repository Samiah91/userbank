from user import User
class BankAccount(User):
    def __init__(self,name,rate=0,account_balance=0): 
        self.name = name
        self.rate = rate
        self.account_balance=account_balance
        

    def deposit(self, amount):
        self.account_balance += amount
        print(self.account_balance,end=" ")
        return self

    def make_withdrawl(self, amount):
        self.account_balance -= amount 
        print(self.account_balance,end =" ")
        return self

    def display(self):
        print(self.name,self.account_balance,end =" ")
        return self

    def yield_interest(self):
        # if rate == 0:
        # print (self.account_balance,self.rate)
        # return self
        print(S.p)
        print(S.r)
        print(S.t)    
        Si=self.p*self.r*self.t/100
        print(Si)   
        return Si 


S=BankAccount("Mark",0,5000)
L=BankAccount("Lee",0,2000)
S.p=5000
S.r=5
S.t=4
L.p=2000
L.r=5
L.t=3
# p=0
# r=0
# t=0

S.deposit(200).deposit(100).deposit(100).make_withdrawl(40).display().yield_interest()
L.deposit(100).deposit(300).make_withdrawl(50).make_withdrawl(50).make_withdrawl(70).make_withdrawl(100).display().yield_interest()