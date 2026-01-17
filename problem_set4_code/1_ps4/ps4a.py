from tree import Node

tree1 = Node(8, Node(2, Node(1), Node(6)), Node(10))
tree2 = Node(7, Node(2, Node(1), Node(5, Node(3), Node(6))), Node(9, Node(8), Node(10)))
tree3 = Node(5, Node(3, Node(2), Node(4)), Node(14, Node(12), Node(21, Node(20), Node(26))))

def find_tree_height(tree):
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    '''
    # Base case: Empty tree height 0('-1')
    if tree is None:
        return -1
    else:
    # Recursive case: height 1 + max height of subtrees
        left_count = find_tree_height(tree.left)
        right_count = find_tree_height(tree.right)
    
    height = 1 + max(left_count, right_count)
    
    return height


def is_heap(tree, compare_func):
    '''
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree
        compare_func: a function that compares the child node value to the parent node value
            i.e. op(child_value,parent_value) for a max heap would return True if child_value < parent_value and False otherwise
                 op(child_value,parent_value) for a min meap would return True if child_value > parent_value and False otherwise
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    '''
    # Base case: If tree is empty, then it is a heap
    if tree is None:
        return True 
    
    # Check left child
    if tree.left is not None:
        # If compare_func returns False, then heap property is violated
        if not compare_func(tree.left.value, tree.value):
            return False
        
        # Recursively check the left subtree
        if not is_heap(tree.left, compare_func):
            return False
     
    # Check right child
    if tree.right is not None:
        # If compare_func returns False, then heap property is violated
        if not compare_func(tree.right.value, tree.value):
            return False
        
        # Recursively check the right subtree
        if not is_heap(tree.right, compare_func):
            return False
    
    # All checks passed
    return True 
    
# max heap comparator
def max_compare_func(child_value, parent_value):
     if child_value < parent_value:
         return True
     return False

# min heap comparator
def min_compare_func(child_value, parent_value):
     if child_value > parent_value:
         return True
     return False
    
# print(is_heap(tree2, max_compare_func))

if __name__ == '__main__':
    tree1_height = find_tree_height(tree1)
    tree2_height = find_tree_height(tree2)
    tree3_height = find_tree_height(tree3)
    
    max_tree1 = is_heap(tree1, max_compare_func)
    max_tree2 = is_heap(tree2, max_compare_func)
    max_tree3 = is_heap(tree3, max_compare_func)
    
    min_tree1 = is_heap(tree1, min_compare_func)
    min_tree2 = is_heap(tree2, min_compare_func)
    min_tree3 = is_heap(tree3, min_compare_func)
    print("")
    print(f"Tree 1, \nheight: {tree1_height}, Is max heap? {max_tree1}, is min heap? {min_tree1}")
    print("________________________________________________________")
    print(f"Tree 2, \nheight: {tree2_height}, Is max heap? {max_tree2}, is min heap? {min_tree2}")
    print("________________________________________________________")
    print(f"Tree 3, \nheight: {tree3_height}, Is max heap? {max_tree3}, is min heap? {min_tree3}")
    print("________________________________________________________")
    
