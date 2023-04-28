'''Define a class Account(ano,name,bal) Define a Customer(amt)
is derive from Account
Write Appropriate methods to accept info of custo and perform deposite method
and new bal'''


class Account:
    def accept(self):
        self.ano=input("Enter account no ")
        self.nm=input("Enter name ")
        self.bal=int(input("Enter balance "))

class Customer(Account):
    def accept_bal(self):
        self.amt=eval(input("Enter amount to deposite"))
        self.bal=self.bal+self.amt
       
    def display(self):
        print("account no ",self.ano)
        print("name ",self.nm)
        print("Balance is ",self.bal)
        
c=Customer()
c.accept();

c.accept_bal();

c.display()




