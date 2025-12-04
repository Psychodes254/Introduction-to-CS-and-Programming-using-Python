#  Hardcode a number as a secret number.
#  Write a program that checks through all the numbers from 1 to
# 10 and prints the secret value if it’s in that range. If it’s not
# found, it doesn’t print anything.

secret = int(input("Type a number: "))

for value in range(1, 11):
    if secret == value:
        print("The secret number is in sequence")
    # else:
    #     pass
