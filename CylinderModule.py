import math
from PointModule import Point
from CircleModule import Circle


class Cylinder(Circle):

    def __init__(self, x, y, radius, height):
        Circle.__init__(self, x, y, radius)
        self.height = float(height)

    def area(self):
        return 2 * Circle.area(self) + \
            2 * math.pi * self.radius * self.height

    def volume(self):
        return Circle.area(self) * self.height

    def __str__(self):
        return "%s; Height = %f" % \
            (Circle.__str__(self), self.height)

    
def main():
    cylinder = Cylinder(12, 23, 2.5, 5.7)

    print("X coordinate is:", cylinder.x)
    print("Y coordinate is:", cylinder.y)
    print("Radius is:", cylinder.radius)
    print("Height is", cylinder.height)

    cylinder.height = 10
    cylinder.radius = 4.25
    cylinder.x, cylinder.y = 2, 2
    print("The new point, radius and height of cylinfer are:", cylinder)
    print("The area of cylinder is: %.2f" % cylinder.area())

    print("cylinder printed as a Point is:", Point.__str__(cylinder))
    print("cylinder printed as a Circle is:", Circle.__str__(cylinder))

if __name__ == '__main__':
    main()
