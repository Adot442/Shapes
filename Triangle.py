from Polygon import Polygon
import math

class Triangle(Polygon):
    
    def getArea(self):
        return round((self.getBase() * self.getHeight() / 2.0), 2)

    def getPerimeter(self):
        return round((self.getBase() + math.sqrt(self.getBase() ** 2 + 4 * self.getHeight() ** 2)), 2)

"""
t = Triangle(7, 5)
print(t.getArea())
"""