# Simple class SimgleList


class SingleList:
    """Documentation for SingleList
    
    """
    def __init__(self, initial_list=None):
        self.__list = []

        if initial_list:
            for value in initial_list:
                if value not in self.__list:
                    self.__list.append(value)

    def __str__(self):
        temp_string = ""
        i = 0

        for i in range(len(self)):
            temp_string += "%12d" % self.__list[i]

            if (i + 1) % 4 == 0:
                temp_string += "\n"

        if i % 4 != 0:
            temp_string += "\n"

        return temp_string

    def __len__(self):
        return len(self.__list)

    def __getitem__(self, index):
        return self.__list[index]

    def __setitem__(self, index, value):
        if value in self.__list:
            raise ValueError("List already contains value %s" % str(value))

        self.__list[index] = value

    def __eq__(self, other):
        if len(self) != len(other):
            return 0

        for i in range(0, len(self)):
            if self.__list[i] != other.__list[i]:
                return 0
        return 1

    def __ne__(self, other):
        return not (self == other)

