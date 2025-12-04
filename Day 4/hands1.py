# Write code that loops a for loop over some range and prints
# how many even numbers are in that range. Try it with:
#  range(5)
#  range(10)
#  range(2,9,3)
#  range(-4,6,2)
#  range(5,6)

count = 0

for i in range(5):
    if i % 2 == 0:
      count += 1
      
      print(count)
      