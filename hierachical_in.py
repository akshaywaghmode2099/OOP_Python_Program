'''Define a Customer(id,name,bal)
Define a Class Saving(total_bal) and Class Current(total_bal)
Both classes Derive from Customer
Accept Customer info and user choice for creating Account then
Calculate interest amount and total bal
For Current Account irate 5%
For Saving Account irate 6.5%*/
'''

class Customer:
    def accept(s):
        s.id=input("Enter account no")
        s.nm=input("Enter name")
        s.bal=eval(input("Enter bal"))

class Saving(Customer):
    def cal(s):
        s.int=s.bal*6.5/100;
        print("name ",s.nm," Accout Type Saving")
        print("balance ",s.bal)
        print("interest amount ",s.int)
        print("Total balance ",s.int+s.bal)

class current(Customer):
    def cal(s):
        s.int=s.bal*5/100;
        print("name ",s.nm,"  Accout Type Current ")
        print("balance ",s.bal)
        print("interest amount ",s.int)
        print("Total balance ",s.int+s.bal)

print("Enter 1.Saving 2.Current ")
t=eval(input("Enter your account type"))
if t==1:
    s=Saving();
    s.accept()
    s.cal()
elif t==2:
    c=current()
    c.accept()
    c.cal()
else:
    print("Enter choice 1 or 2 ")






