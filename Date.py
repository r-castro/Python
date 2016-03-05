class Date:

    daysPerMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, mounth, day, year):

        if 0 < mounth <= 12:
            self.mounth = mounth
        else:
            raise ValueError("Invalid value for mounth: %d" % mounth)

        if year >= 0:
            self.year = year
        else:
            raise ValueError("Invalid value for year: %y" % year)

        self.day = self.checkDay(day)

        print("Date constructior:", self.display())

    def __del__(self):
        print("Date object about to be destroyed:", self.display())

    def display(self):
        return "%d/%d/%d" % (self.mounth, self.day, self.year)

    def checkDay(self, testDay):
        if 0 < testDay <= Date.daysPerMonth[self.mounth]:
            return testDay
        elif self.mounth == 2 and testDay == 29 and (self.year % 400 == 0 or
                                                     self.year % 100 != 0 and
                                                     self.year % 4 == 0):
            return testDay
        else:
            raise ValueError("Invalid day: %d for mounth: %d" %
                             (testDay, self.mounth))

