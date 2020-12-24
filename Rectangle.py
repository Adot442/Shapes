from Polygon import Polygon 
import math
class Rectangle(Polygon):
    
    def getArea(self):
        return (self.getBase() * math.sqrt(self.getHeight() ** 2))

    def getPerimeter(self):
        return round((self.getBase() + self.getHeight()) * 2.0, 2)

s = Rectangle(11, 13)

print(s.getPerimeter())