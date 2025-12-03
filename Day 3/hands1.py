# Expand this code to show a sad face when the user entered the
# while loop more than 2 times.
#  Hint: use a variable as a counter

where = input("Go left or right? ")

n = 1

while where == "right":
    
    where = input("Go left or right? ")
    
    n += 1
    
    if n > 1:
        print("😒")
        
print("You got out!")