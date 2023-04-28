class Demo:     #parent
    def show(self):
        print("in show")

    def display(self):
        print("in display ")

class Check(Demo):  #child
    def test(self):
        print("in test ")



c=Check()
c.test()
c.show()
