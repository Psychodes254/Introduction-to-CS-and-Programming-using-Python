import random
import string

WORDLIST_FILENAME = "words.txt"

# Load the word.txt file
def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist


# Select one of the word randomly in wordlist
def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    word = list(secret_word)
    
    for char in word:
        if char not in letters_guessed: 
            return False
    return True


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    result_list = []
    char = list(secret_word)
    
    for i in range(len(secret_word)):
        if char[i] in letters_guessed:
            result_list.append(char[i])
        else:
            result_list.append("*")
            
    results = "".join(result_list)
            
    return results


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    alphabets = string.ascii_lowercase
    
    for char in letters_guessed:
        alphabets = alphabets.replace(char, "")
    return alphabets


def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    
    print("Welcome to Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    
    guess = 10
    letters = get_available_letters
    letter_guessed = []
    result = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    # The game loop
    while guess > 0:
        print("-------------------")
        print(f"You have {guess} guesses left.")
        print(f"Available letters: {letters(letter_guessed)}")
        
        user_input = input("Please guess a letter: ").lower()
        
        # If user input is the special letter "!" print the one hint, then deduct 3 guesses if guess is > 3
        if user_input == "!" and with_help:
            if guess > 3:
                guess -= 3
                for char in secret_word:
                    if char not in letter_guessed:
                        letter_guessed.append(char)
                        revealed = get_word_progress(secret_word, letter_guessed)
                        print(f"Letter revealed: {char}")
                        print(f"{revealed}")
                        break
            else:
                print(f"You currently have {guess} guess left")
            continue
            
        # Validate if user input is correct
        if user_input not in string.ascii_lowercase or len(user_input) > 1:
            print(f"Oops! That is not a valid letter. Please input a letter from the alphabet: {result}")
            continue
        
        # Check if user input is already guessed
        if user_input in letter_guessed:
            guess -= 2
            print(f"Oops! You've already guessed that letter: {result}")
            continue
        
        # If the user input has passed all the validation, add to guessed list, then check the word progress function
        letter_guessed.append(user_input)
        result = get_word_progress(secret_word, letter_guessed)
        
        # Check if guess is correct
        if user_input in secret_word:
            print(f"Good guess: {result}")
        else:
            guess -= 1
            if user_input in vowels:
                guess -= 1
            print(f"Oops! That letter is not in my word: {result}")
            
        # Calculate the total score
        total_score = (guess + 4 * len(secret_word)) + (3 + len(secret_word))
           
        # Check win condition
        if has_player_won(secret_word, letter_guessed):
            print("-------------------")
            print("Congratulations, you won!")
            print(f"Your total score for this game is: {total_score}")
            break
    
    # Loss condition
    if guess < 1:    
        print("-------------------")
        print(f"Sorry, you ran out of guesses. The word was {secret_word}.")

if __name__ == "__main__":

    secret_word = choose_word(wordlist)
    with_help = True
    hangman(secret_word, with_help)