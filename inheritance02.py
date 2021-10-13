class Person:
    country = "India"
    def takeBreath(self):
        print("I am Breathing")
class Employee:
    company = "Honda"
    def getSalary(self):
        print(f"Salary is {self.salary}")
    def takeBreath(self):
        print(f"I am employee so I am luckily Breathing")
class Programmer(Employee):
    company = "Fiverr"
    def getSalary(self):
        print(f"No salary to programmers")
    def tekeBreath(self):
        print(f"I am an employee so I am luckily Breathing++")
p = Person()
p.takeBreath()
e = Employee()
e.takeBreath()
print(e.company)
pr = Programmer()
pr.takeBreath()
print(pr.company)
print(p.country)