#  How does the program look if I change the requirement to be:
# If it’s not found, prints that it didn’t find it.

found = False
secret = int(input("Type a number: "))

for value in range(1, 11):
    if  value == secret:
        found = True
        continue
        # print("Found!")
if not found:
    print("Not found!")
        