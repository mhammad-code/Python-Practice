class Student:
    def __init__(self, name, age, rollno):
        self.name = name
        self.age = age
        self.rollno = rollno
    def display(self):
        print(self.name, self.age, self.rollno)


student1 = Student("John", 22, 22)
student1.display()