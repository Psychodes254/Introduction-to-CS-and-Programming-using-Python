def find_grades(grades, students):
    """ grades is a dictmapping student names (str) to grades (str)
    students is a list of student names
    Returns a list containing the grades for students (in same order) """
    
    values = []
    
    for x in students:
        values.append(grades[x])
    
    return values

d = {'Ana':'B', 'Matt':'C', 'John':'B', 'Katy':'A'}
print(find_grades(d, ['Matt', 'Katy'])) # returns ['C', 'A']