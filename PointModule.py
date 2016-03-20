# Definition and test function for class Point


class Point:

    def __init__(self, x_value=0, y_value=0):
        self.x = x_value
        self.y = y_value

    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)


def main():
    point = Point(72, 115)

    print("X coodinate is:", point.x)
    print("Y coodinate is:", point.y)

    point.x = 10
    point.y = 10

    print("The new location of point is:", point)


if __name__ == "__main__":
    main()
