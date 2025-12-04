# Assume you are given a string of lowercase letters in variable s.
# Count how many unique letters there are in the string. For
# example, if
# s = "abca"
# Then your code prints 3. 

letters = input("Give some letter: ").lower()

seen = ""
for s in letters:
    if s in letters:
        if s not in seen:
            seen += s
        
print(len(seen))