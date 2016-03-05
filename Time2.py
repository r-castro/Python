# Class Time with accessor methods.


class Time:
    """Documentation for Time
    
    """
    def __init__(self):
        self._hour = 0
        self._minute = 0
        self._second = 0

    def time(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, hour):
        if 0 <= hour < 24:
            self._hour = hour
        else:
            raise ValueError("Invalid hour value: %d" % hour)

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, minute):
        if 0 <= minute < 60:
            self._minute = minute
        else:
            raise ValueError("Invalid minute value: %d" % minute)

    @property
    def second(self):
        return self.second

    @second.setter
    def second(self, second):
        if 0 <= second < 60:
            self._second = second
        else:
            raise ValueError("Invalid second value: %d" % second)

    def print_military(self):
        return "%.2d:%.2d:%.2d" % (self._hour, self._minute, self._second)

    def print_standard(self):
        standard_time = ""

        if self._hour == 0 or self._hour == 12:
            standard_time += "12:"
        else:
            standard_time += "%d:" % (self._hour % 12)

        standard_time += "%.2d:%.2d" % (self._minute, self._second)

        if self._hour < 12:
            standard_time += " AM"
        else:
            standard_time += " PM"

        return standard_time
