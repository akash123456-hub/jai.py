class Employee:
    company = "Google"
    salary = 2000
    location = "Delhi"
    @classmethod
    def changeSalary(cls,sal):
        cls.salary = sal
e = Employee()
print(e.salary)
e.changeSalary(2100)
print(e.salary)
print(Employee.salary)
