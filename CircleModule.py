import math
from PointModule import Point


class Circle(Point):
    """Documentation for Circle
    
    """
    def __init__(self, x=0, y=0, radiusValue=0.0):
        Point.__init__(self, x, y)
        self.radius = float(radiusValue)

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return "Center  = %s Radius = %f" % \
            (Point.__str__(self), self.radius)

   
def main():
    circle = Circle(37, 43, 2.5)

    print("X coordinate is", circle.x)
    print("Y coordinate is", circle.y)
    print("Radius is:", circle.radius)

    circle.radius = 4.25
    circle.x = 2
    circle.y = 2

    print("The new location and radius of circle are:", circle)
    print("The area of circle is: %.2f" % circle.area())

    print("circle printed as a Point is:", Point.__str__(circle))

if __name__ == '__main__':
    main()
