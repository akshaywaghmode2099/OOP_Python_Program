'''Define a class Customer name,shopping amount as data member
if amount 1000-5000 get 10%discount on shopping amount
amount 5000-8000 get 15% discount on shopping amount
amount>8000 get 25% discount on shopping amount
calculate discount and payable amount of customer'''

class Customer:
    def accept(self):
        self.nm=(input("Enter customer name"))
        self.amt=eval(input("Enter shopping amount"))

    def cal(self):
        if self.amt>=1000 and self.amt<5000:
            dis=self.amt*(10/100)

        elif 5000<=self.amt<8000:
             dis=self.amt*(15/100)
        elif self.amt>=8000:
             dis=self.amt*(25/100)
        else:
            dis=0

        pay_Amt=self.amt-dis
        print("name ",self.nm)
        print("Shopping amount ",self.amt)
        print("Discunt ",dis)
        print("payable amount ",pay_Amt)


c=Customer()
c.accept()
c.cal()






        
