'''Assignment:
Create a class Employee with:

a public variable name,

a protected variable _salary, and

a private variable __ssn.

Try accessing all three variables from an object of the class and document what happens.

'''

class Employee:
    def __init__(self,name , salary , ssn ):

        self.name = name #public
        self._salary = salary #protected
        self.__ssn = ssn #private           
emp = Employee("Hafeez", 50000, "03062354880")

print(emp.name)
print(emp._salary)
#print(emp.__ssn)
print(emp._Employee__ssn)

