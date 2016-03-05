from Date import Date


class Employee():
    """Documentation for Employee
    
    """
    def __init__(self, firstName, lastName, birthMonth, birthDay,
                 birthYear, hireMonth, hireDay, hireYear):

        self.birthDate = Date(birthMonth, birthDay, birthYear)
        self.hireDate = Date(hireMonth, hireDay, hireYear)

        self.lastName = lastName
        self.firstName = firstName

        print("Employee construction: %s, %s" % (self.lastName,
                                                 self.firstName))

    def __del__(self):
        print("Employee object about to be destroyed: %s, %s"
              % (self.lastName, self.firstName))

    def display(self):
        print ("%s, %s\nHired:%s\nBirth Date:%s\n" %
               (self.lastName, self.firstName, self.hireDate.display(),
                self.birthDate.display()))
