from Triangle import Triangle
from Rectangle import Rectangle

def main():
    t = Triangle(4, 3)
    s = Rectangle(8, 8)
    #print("Base is: " + str(p.base))
    #print("Height is: " + str(p.height))
    print("Area is: " + str(t.getArea()))
    print("Perimeter is: " + str(t.getPerimeter()))
    print("Area is: " + str(s.getArea()))
    print("Perimeter is: " + str(s.getPerimeter()))

main()