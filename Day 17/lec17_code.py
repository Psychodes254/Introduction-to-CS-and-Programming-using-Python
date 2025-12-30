class Coordinate(object):
    """ A coordinate made up of an x and y numerical value """
    def __init__(self, x, y):
        """ Sets the x and y values """
        self.x = x
        self.y = y
    def getX(self):
        """ Returns how far away self is on the x axis """
        return self.x
    def getY(self):
        """ Returns how far away self is on the y axis """
        return self.y
    def distance(self, other):
        """ Returns the euclidean distance between two Coordinate objects """
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

c = Coordinate(3,4)
a = 0
origin = Coordinate(a,a)

# these 3 calls returns the same thing
# print(c.distance(origin))
# print(Coordinate.distance(c, origin))
# print(origin.distance(c))


################ AT HOME #####################
# Write a class definition for a vehicle. A vehicle is defined by attributes:
# Number of wheels
# Number of occupants
# Color 
# Decide the type of each data attribute and document this
class Vehicle(object):
    def __init__(self, w, o, c="Black"):
        """Wheel and Occupants must be Integers, while Color is a String"""
        if not type(w) == int and type(o) == int:
            raise ValueError("Wheel must be an integer!")
        if not type(c) == str:
            raise ValueError("Color must be a string!")
            
        self.wheel = w
        self.occupants = o
        self.color = c
        self.max_occupancy = 5
        
    def get_wheel(self):
        """Returns the Wheel of self"""
        return self.wheel
    
    def get_occupants(self):
        """Returns the Occupants of self"""
        return self.occupants
    
    def get_color(self):
        """Returns the Color of self"""
        return self.color
    
    def add_n_occupants(self, n):
        """Adding the number of occupants, if it exceeds the max occupancy, it raises a ValueError"""
        if self.occupants + n > self.max_occupancy:
            raise ValueError("Car can't exceed 5 people!")
        else:
            return self.occupants + n

# Examples:    
wheel = 4
occupants = 5
color = "red"
    
v = Vehicle(wheel, occupants, color)
# print(v.get_wheel())
# print(v.get_occupants())
# print(v.get_color())
# _________________________________________________________

car1 = Vehicle(2, 1, "Red")
car2 = Vehicle(18, 3, "Green")
# print(car1.get_occupants())
# print(car2.get_color())
# _________________________________________________________
        
v1 = Vehicle(4,2,'blue')
# print(v1.get_occupants())   # prints 2
# print(v1.add_n_occupants(3))   # prints 5
# print(v1.get_occupants())
# print(v1.add_n_occupants(4)) # raises ValueError
