"""
Your task is to complete the implementation of the functions below, which do some kind of
manipulation of linked lists (that is, you need to use the LinkedList class defined in the p0 session)
"""

from linked_list import LinkedList


def find(L, e):
    """
    This function should look for an element in a linked list and prints on the console the result of the search
     e.g. "Element not found in the list", "Element X found in the list at position Y"
    :param L: the list
    :param e: the element to look for
    """
    pos = 1
    walk = L._head
    while walk is not None:
        if walk._data == e:
            print("Element " + str(e) + "found in the list at position " + str(pos))
            return
        walk = walk._next
        pos += 1
    print("Element " + str(e) + " not found in the list")
    return


def cat(L1,L2):
    """
    This function should append the content of one list L2 at the end of the list L1. in other words, this
    function "concatenates" L1 and L2.
    (Therefore, L1 is modified as an effect of the execution of this function)
    Example: L1 = 10 -> 20 -> 5   ; L2 = 89 -> 56 -> 80
    After executiing the function, it will be: L1 = 10 -> 20 -> 5  -> 89 -> 56 -> 80 ; L2 = 89 -> 56 -> 80
    """
    current = L2._head

    while current:
        L1.add_last(current._data)
        current = current._next
    
    return L1


def copy(L):
    """
    This function returns a new list which is a copy of the list L.
    This function returns a "deep" copy of the list L, that is, a new list whose element are the same
    as L (and in the same order).
    Hint for the implementation: The LinkedList allows to add elements only at the "head" of a linked list...so...
    :param L: the list to copy
    :return: a "deep" copy of the list L
    """
    new = LinkedList()
    walk = L._head
    pos = 0
    while walk is not None:
        new.insert_at_position(pos, walk._data)
        pos += 1
        walk = walk._next
    return new

def copy_and_cat(L1,L2):
    """
    This function should return a new list that is the concatenation of two lists L1 and L2.
    That is, the lists L1 and L2 should NOT be modified by this function
    (Hint: make a "deep copy" of the two lists and build the returned lists using these copies...)
    :param L1:
    :param L2:
    :return: a list containing the concatenation of L1 and L2
    """
    new = LinkedList()

    current = L1._head

    while current:
        new.append(current._data)
        current = current._next
    
    current = L2._head
    
    while current:
        new.append(current._data)
        current = current._next
    
    return new


def len_recursive(node):
    """
    This function should calculate the length of a linked list recursively
    :param node: the head of the list
    :return: the length of the list
    """
    if node._next == None:
        return 1
    return len_recursive(node._next) + 1

""" main() to do some testing"""
if __name__ == '__main__':
    L1 = LinkedList()
    L2 = LinkedList()
    L1.add_first("Jin")
    L1.add_first("Jun")
    L1.add_first("Jan")
    L1.print()
    L2.add_first(118)
    L2.add_first(115)
    L2.add_first(89)
    L2.add_first(87)
    L2.print()
    find(L1,"Jin")
    find(L1, 908)
    cat(L1,L2)
    L1.print()
    len_l2 = len_recursive(L2._head)
    print("Length of list is: {0}".format(len_l2))
    print("Length of list is: {0}".format(len_recursive(L1._head)))
    print("""Test deep copy and copy_cat""")
    L3 = copy(L1)
    L3.print()
    L3.add_first("new")
    L3.print()
    L1.print()
    L4 = copy_and_cat(L1,L3)
    L4.print()
