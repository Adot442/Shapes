class Polygon:
    """
    docstring
    """
    def __init__(self, base, height):
        self.__height = height
        self.__base = base

    def getBase(self):
        return self.__base
    
    def getHeight(self):
        return self.__height

    def setHeight(self, h):
        self.__height = h
    
    def setBase(self, b):
        self.__base = b


