'''Define a class Student having id,name Define a class marks 
having marks of 4 subject it is derive from Student Define a
Result having total,per it is derive Marks.
Write approriate method and calculate result of 2 students'''


class student:
    def accept(s):
        s.id=int(input("enter student id"))
        s.name=input("enter student name")


class Marks(student):
    def accept_mark(s):
        s.m1=int(input("Enter Subject1 marks "))
        s.m2=int(input("Enter Subject2 marks "))
        s.m3=int(input("Enter Subject3 marks "))
        s.m4=int(input("Enter Subject4 marks "))

class Result(Marks):
    def cal(s):
        if(s.m1>=40 and s.m2>=40 and s.m3>=40 and s.m4>=40):
            s.str="pass"
        else:
            s.str="fail"
        s.total=s.m1+s.m2+s.m3+s.m4
        s.per=s.total/4

    def display(s):
        print("Result is ")
        print("rno ",s.id," name ",s.name)
        print("total ",s.total,"/400  percentage ",s.per)
        print(s.str)
        
s1=Result()
s1.accept()
s1.accept_mark()

s2=Result()
s2.accept()
s2.accept_mark()

print("============output=========")

s1.cal()
s1.display()
s2.cal()
s2.display()


        
