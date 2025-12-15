# Write a function that meets these specs:
    
def sort_words(sen):
    """ sen is a string representing a sentence
    Returns a list containing all the words in senbut
    sorted in alphabetical order. """
    
    
    new_list = sen.split(' ')
    new_list.sort()
    
    return new_list
    
print(sort_words("look at this photograph"))