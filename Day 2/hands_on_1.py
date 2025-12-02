# Write a program that
#  Asks the user for a verb
#  Prints “I can _ better than you” where you replace _ with the verb.
#  Then prints the verb 5 times in a row separated by spaces.
#  For example, if the user enters run, you print:
# I can run better than you!
# run run run run run

verb = input("Type a verb: ")

print(f"I can {verb} better than you!" "\n" f"{(verb + " ") * 5 } ")

