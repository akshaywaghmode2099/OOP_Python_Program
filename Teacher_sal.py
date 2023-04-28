'''Define a class Teacher accept teacher name and monthy sal
and calculate aanual sal
Write appropriate method to accept Teacher info and cal
if sal more than 300000 then cal tax , tax is 5% on sal'''

class Teacher:
    def accept(self):
        self.nm=(input("Enter name"))
        self.m=eval(input("Enter monthly salary "))

    def cal(self):
        self.annual=self.m*12
        if(self.annual>300000):
            tax=self.annual*(5/100)
        else:
            tax=0
        print("name ",self.nm)
        print("Annual salary ",self.annual)
        print("Tax ",tax)
        

t=Teacher()
t.accept()
t.cal()
