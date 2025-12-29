class Container(object):
    """
    A container object is a list and can store elements of any type
    """
    def __init__(self):
        """
        Initializes an empty list
        """
        self.myList = []

    def size(self):
        """
        Returns the length of the container list
        """
        return len(self.myList)

    def add(self, elem):
        """
        Adds the elem to one end of the container list, keeping the end
        you add to consistent. Does not return anything
        """
        self.myList.append(elem)

class Queue(Container):
    """
    A subclass of Container. Has an additional method to remove elements.
    """   
    def remove(self):
        """
        The oldest element in the container list is removed
        Returns the element removed or None if the stack contains no elements
        """
        s = super().size()
        if s > 0:
            removed_elem = self.myList.pop(0)
            return removed_elem
        else:
            return
    
# Examples:
q = Queue()
# print(q.remove())        # None

q.add(1)
q.add(2)
q.add(3)

# print(q.remove())        # 1
# print(q.remove())        # 2
# print(q.size())          # 1


