# Class Time with accessor methods.


class Time:
    """Documentation for Time
    
    """
    def __init__(self, hour=0, minute=0, second=0):
        self.time(hour, minute, second)

    def time(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, hour):
        if 0 <= hour < 24:
            self.__hour = hour
        else:
            raise ValueError("Invalid hour value: %d" % hour)

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, minute):
        if 0 <= minute < 60:
            self.__minute = minute
        else:
            raise ValueError("Invalid minute value: %d" % minute)

    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, second):
        if 0 <= second < 60:
            self.__second = second
        else:
            raise ValueError("Invalid second value: %d" % second)

    def print_military(self):
        return "%.2d:%.2d:%.2d" % (self.__hour, self.__minute, self.__second)

    def print_standard(self):
        standard_time = ""

        if self.__hour == 0 or self.__hour == 12:
            standard_time += "12:"
        else:
            standard_time += "%d:" % (self.__hour % 12)

        standard_time += "%.2d:%.2d" % (self.__minute, self.__second)

        if self.__hour < 12:
            standard_time += " AM"
        else:
            standard_time += " PM"

        return standard_time
