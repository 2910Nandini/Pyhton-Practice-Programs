#to find area and circumference of a circle using classes

class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
    def circumference(self):
        return 2*3.14*self.radius

circle1=circle(int(input("enter radius")))
a=circle1.area()
print("area= ",a)
b=circle1.circumference()
print("circumference= ",b)
