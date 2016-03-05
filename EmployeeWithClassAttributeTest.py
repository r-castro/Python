from EmployeeWithClassAttribute import Employee

print("Number of employees before instantiation is", Employee.Count)

employee1 = Employee("Susan", "Baker")
employee2 = Employee("Robert", "Jones")
employee3 = employee1

print("Number of employees after instantiation is",
      employee1.Count)

del employee1
del employee2
del employee3

print("Number of employees after deletion is", Employee.Count)
