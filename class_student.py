class student:
    def __init__ (self,rollno,name,course):
        self.rollno=rollno
        self.name=name
        self.course=course
    def displaystudent(self):
        print("Rollno",self.rollno)
        print("Name",self.name)
        print("course",self.course)
stud1=student(10,"Jack","MCA")
stud2=student(3,"Anu","MSC")
stud1.displaystudent()
stud2.displaystudent()
