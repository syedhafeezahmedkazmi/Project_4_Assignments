
'''Assignment:
Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.'''


class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name} Marks: {self.marks} ")

s1 = Student("Hafeez" , 97)
#print(s1.name)
#print(s1.marks)

s1.display()
