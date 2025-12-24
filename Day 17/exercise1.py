class Circle():
    def __init__(self, radius):
        """ Initializes self with radius """
        self.r = radius

    def get_radius(self):
        """ Returns the radius of self """
        return self.r

    def set_radius(self, radius):
        """ radius is a number
        Changes the radius of self to radius """
        self.r = radius

    def get_area(self):
        """ Returns the area of self using pi = 3.14 """
        area = 3.14 * self.r * self.r
        return area

    def equal(self, c):
        """ c is a Circle object
        Returns True if self and c have the same radius value """
        return c.r == self.r

    def bigger(self, c):
        """ c is a Circle object
        Returns self or c, the Circle object with the bigger radius """
        if c.r > self.r:
            return c
        else:
            return self
        
obj = Circle(4)
print(obj.get_radius())