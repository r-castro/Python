class Employee:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def __str__(self):
        return "%s %s" % (self.firstname, self.lastname)

    
class HourlyWorker(Employee):

    def __init__(self, first, last, initHours, initWage):
        Employee.__init__(self, first, last)
        self.hours = float(initHours)
        self.wage = float(initWage)

    def getPay(self):
        return self.hours * self.wage

    def __str__(self):
        print("HorlyWorker.__str__ is executing""")

        return "%s is an hourly worker with pay of $%.2f" % \
            (Employee.__str__(self), self.getPay())

hourly = HourlyWorker("Bob", "Smith", 40.0, 10.00)

print("Calling __str__ several ways...")

print(HourlyWorker.__str__(hourly))
