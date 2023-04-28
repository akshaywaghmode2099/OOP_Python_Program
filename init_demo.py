class Demo:
    __num=100  #private
    def display(self):
        print("n = ",self.n,"d = ",self.d)

    def __init__(self,num=0,den=0):
        self.n=num
        self.d=den
        print(Demo.__num)
    def __del__(self):
        print("in destructor ")

        
ob1=Demo(3,4)
ob1.display()



#ob1.display()Error

