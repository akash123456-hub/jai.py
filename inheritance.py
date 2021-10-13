class Employee:
    company = "Google"
    salary = 30000
jai = Employee()
alka = Employee()
Employee.company = "Youtube"
print(jai.company)
jai.salary = 3000
print(jai.salary)