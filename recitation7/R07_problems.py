# Problem 1: 
# Write a function that takes as input a dictionary and returns a new dictionary,
# where 5 is added to each value of the original dictionary, assuming all values are integers.
def new_dict(input_dict):
    for k, v in input_dict.items():
        input_dict[k] = v + 5
    return input_dict
    
input_dict = {"item1": 2, "item2": 7, "item3": 20}
# print(new_dict({"item1": 2, "item2": 7, "item3": 20})) # expect {"item1": 7, "item2": 12, "item3": 25}


# Problem 2:
# Write a function to check all values are same in a dictionary. 
# Return True if they are all the same, False otherwise
def check_same_values(input_dict):
    for value in input_dict.values():
        for value2 in input_dict.values():
            if value != value2:
                return False
    return True

input_dict = {'item1': 'apple', 'item2': 'apple', 'item3': 'apple'}
# print(check_same_values(input_dict))
input_dict = {'item1': 'apple', 'item2': 'apple', 'item3': 'orange'}
# print(check_same_values(input_dict))



# Problem 3: 
# Convert a dictionary to a list of lists where each sublist is in the 
# form [key, value]. Return a sorted version of this list where we sort 
# by decreasing values. 
def dict_to_sorted_list(input_dict):
    new_dict = []
    for k, v in input_dict.items():
        new_dict.append([k, v])
    
    new_dict.sort(key=lambda x: x[1], reverse=True)
        
    return new_dict

input_dict = {'a': 1, 'b': 5, 'c': 10, 'd': 3, 'e': 2}  
# print(dict_to_sorted_list(input_dict))


# Problem 4:
# Given a list of dictionaries with item names and amounts in the form {'item': 'my_item_name', 'amount': 'my_amount'}
# write function to combine these items into a single dictionary.
def combine_dicts(input_dicts):
    comb_dict = {}
    comb_lst = []
    
    for elem in input_dicts:
        comb_lst.append((list(elem.values())))
        
    for val in comb_lst:
        if val[0] not in comb_dict:
            comb_dict[val[0]] = val[1]
        else:
            comb_dict[val[0]] += val[1]
            
    return comb_dict
# testing
input_dicts = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# print(combine_dicts(input_dicts)) 


    