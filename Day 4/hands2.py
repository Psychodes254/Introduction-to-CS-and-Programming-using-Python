an_letters = "aeiou"

word = input("I will cheer for you! Give a word: ")

times = int(input("How many times do you want to be cheered? "))

for w in word:
    if w in an_letters:
        print(f"Give me an {w}: {w}")
    else:
        print(f"Give me a {w}: {w}")

print("What does that spell!")
for i in range(times):
    print(word)
    