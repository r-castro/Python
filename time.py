# Simple definition of class time


class Time:
    """Time abstract data type (ADT) definition"""

    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.second = 0

    def print_military(self):
        return "%.2d:%.2d:%.2d" % (self.hour, self.minute, self.second)

    def print_standard(self):
        standard_time = ""

        if self.hour == 0 or self.hour == 12:
            standard_time += "12:"
        else:
            standard_time += "%d:" % (self.hour % 12)

        standard_time += "%.2d:%.2d" % (self.minute, self.second)

        if self.hour < 12:
            standard_time += " AM"
        else:
            standard_time += " PM"

        return standard_time
