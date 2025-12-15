# Write a function that meets these specs:
    
def count_words(sen):
    """ senis a string representing a sentence
    Returns how many words are in s (i.e. a word is a
    a sequence of characters between spaces. """
    
    words = sen.split(' ')
    return len(words)
    
print(count_words("Hello it's me"))