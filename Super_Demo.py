class Demo:
    def show(self):
        print("in Demo ")

class Test(Demo):
    def show(self):
        super().show()
        print("in test ")
       

'''t1=Demo()
t1.show()
'''
t=Test()
t.show()

