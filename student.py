'''Define a student accept student name marks of 3 subjects and
calculate total and percentage of student
Write appropriate method to accept student info and cal result'''


class Student:
    def accept(self):
        self.nm=(input("Enter name"))
        self.m1=eval(input("Enter subject1 marks"))
        self.m2=eval(input("Enter subject2 marks"))
        self.m3=eval(input("Enter subject3 marks"))

    def cal(self):
        self.total=self.m1+self.m2+self.m3
        self.per=(self.total/300)*100
        print("student name ",self.nm)
        print("student total ",self.total,"/300")
        print("student percentage ",self.per,"%")

s1=Student()
s1.accept()

s2=Student()
s2.accept()

s1.cal()
s2.cal()



