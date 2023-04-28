class Add:
    no=100
    def add(self,a,b):
        self.a=a
        self.x=b
        print("Addition ",self.a+self.x)
        print(Add.no)

    def show(s):
        print(s.a)

    @classmethod
    def change(cls):
        cls.no=500
        
    @staticmethod
    def avg(a,b):
        print("avg ",a+b/2)
        
ob=Add();
ob.add(3,3)
ob.show()
Add.avg(12,33)

'''
Add.change() #call class method using class name
ob1=Add()
ob1.add(23,4)'''
