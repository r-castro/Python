class Employee:
    Count = 0
    """Documentation for Employee
    
    """
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last
        Employee.Count += 1
        print("Employee constructor for %s, %s" %
              (self.lastname, self.firstname))

    def __del__(self):
        print("Employee destructor for %s, %s" %
              (self.lastname, self.firstname))
        Employee.Count -= 1
