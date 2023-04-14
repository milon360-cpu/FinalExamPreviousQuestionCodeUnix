'''
Question6:
Write a python script to create a class name student that contains a
construction to initilize
The student name, department, completes credits and total credits. A methods
name remaining_credit() of the class will calculate credits of the student and
print the students name department total credits and the remaining credits
value
'''
class Student:
    def __init__(self,name,dept,comCredits,totalCredits):
        self.name = name
        self.dept = dept
        self.comCredits = comCredits
        self.totalCredits = totalCredits 
    def remaining_credit(self):
        print("Student Name: ",self.name)
        print("Department: ",self.dept)
        print("Total Credits: ",self.totalCredits)
        print("Remaining Credits",self.totalCredits - self.comCredits) 


student = Student("Milon Mondal","CSE",120,164)
student.remaining_credit()