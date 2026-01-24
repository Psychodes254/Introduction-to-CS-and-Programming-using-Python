# Practice Problem 1
# Write a program that takes your name as an Input and Outputs the length of your name minus 5.

user_input = input("Type your name: ")
print((len(user_input) -5))


# Practice Problem 2
# Write a program to remove the nth character from a non empty string.
# Print the old string and the new string.
test_string = "We want to remove the nth character from this string"
n = 8

str_list = list(test_string)
str_list.pop(n-1)
new_str = "".join(char for char in str_list)

print(test_string)
print(new_str)


# Practice Problem 3
# Write a program which answers the following:
# Does a given string have length greater than 10 or less than 5? If True, output True. If False, output False.
my_string = "This is my string"

if len(my_string) > 10 or len(my_string) < 5:
    print(True)
else:
    print(False)


# Practice Problem 4
# Write a program which answers the following using a for loop:
# Count the number of e's in the following string
my_string = "How many times is the letter e in this string?"

count = 0
for char in my_string:
    if char == 'e':
        count += 1
print(count)