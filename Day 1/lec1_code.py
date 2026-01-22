## CHECK THE TYPE OF OBJECTS ##
type(5) # int
type(3.0) # float

## CONVERT TO ANOTHER TYPE ##
float(3) # 3.0
int(3.9) # 3
round(3.9) # 4

## EXPRESSIONS ##
3+2 # 5
(4+2)*6-1 # 35
type((4+2)*6-1) # int
float((4+2)*6-1) # 35.0

## VARIABLES ##
pi = 355/113 

# Compute approximate value for pi
pi = 355/113
radius = 2.2
area = pi*(radius**2) # 15.205309734513278
circumference = pi*(radius*2) # 13.823008849557525


## CODE STYLE ##
# Example 1
#do calculations
a = 355/113 *(2.2**2)
c = 355/113 *(2.2*2)

# Example 2
p = 355/113
r = 2.2
#multiply p with r squared
a = p*(r**2)
#multiply p with r times 2
c = p*(r*2)

#Example 3
#calculate area and circumference of a circle using an approximation for pi
pi = 355/113
radius = 2.2
area = pi*(radius**2)
circumference = pi*(radius*2)

## CHANGING BINDINGS ##
pi = 3.14
radius = 2.2
area = pi*(radius**2)
radius = radius+1


## DEBUG THIS - SWAP VALUES ##
# Given x and y below, the code incorrectly swaps the values. Fix it!
x = 1			
y = 2

b = x 
x = y
y = b

# -----OR-------
x, y = 2, 1
