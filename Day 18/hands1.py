# Add code to the initmethod to check that the type of center 
# is a Coordinate obj and the type of radius is an int. 
# If either are not these types, raise a ValueError.

class Coordinate(object):
    """ A coordinate made up of an x and y value """
    def __init__(self, x, y):
        """ Sets the x and y values """
        self.x = x
        self.y = y
    def distance(self, other):
        """ Returns the euclidean distance between two Coordinate objects """
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    def to_origin(self):
        """ always sets self.x and self.y to 0,0 """
        self.x = 0
        self.y = 0
    def __str__(self):
        """ Returns a string representation of self """
        return "<" + str(self.x) + "," + str(self.y) + ">"

class Circle(object):
    def __init__(self, center, radius):
        if not isinstance(center, Coordinate):
            raise ValueError("Center must be a coordinate object!")
            
        if not isinstance(radius, int):
            raise ValueError("Radius must be an integer!")
            
        self.center = center
        self.radius = radius
        

# center = Coordinate(2, 2)
# my_circle = Circle(center, 2)   # no error

# my_circle = Circle(2, 2)    # raises ValueError
# my_circle = Circle(center, 'two')  # raises ValueError