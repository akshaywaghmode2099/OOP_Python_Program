class Test:
    clg="modern";   #class
    def accept(s,name,no):
        s.name=name        #instance variable
        print("name ",name)

    def show(se):
        print("in show")
        print("name ",se.name,"college name ",Test.clg)

    def change(s):
        Test.clg="FC"
        
t=Test()    #t is object of test class
t.accept('priya',8)
t.show()

t1=Test()    #t is object of test class
t1.accept('Kavya',18)
t1.show()

t.change()

t1.show()
t.show();
