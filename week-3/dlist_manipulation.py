"""
Your task is to complete the implementation of the functions below, which do some kind of
manipulation of DOUBLY linked lists (that is, you need to use the DoublyLinkedList class defined in the p0 session)

Note the import of the Node class, this is needed if you need to create new nodes to insert into
a list
"""

from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import Node

def swap_first_with_last(DL):
    """
    This function should swap the content of the head of the doubly linked list with the content of its tail.
    E.g. swap_first_with_last() applied to 10 <-> 67 <-> 87 <-> 9 returns 9 <-> 67 <-> 87 <-> 10]
    :param DL: a doubly linked list
    """
    temp = DL._head._data
    DL._head._data = DL._tail._data
    DL._tail._data = temp
    return


def insert_at_position(DL, n, data):
    """
    This function should insert an element in a doubly linked list at a specific position.
    E.g. After executing insert_at_position(DL, 2, 88) with DL = 10 <-> 67 <-> 87 <-> 9
    It should be DL =  10 <-> 88 <-> 67 <-> 87 <-> 9
    Note 1: try to implement this function in the fastest way possible (...how?)
    Note 2: be careful at how you manage insertion at the head of the list (position 1) and at the tail (position DL.__len__())
    :param DL: a doubly linked list
    :param n: the position at which n should be inserted
    :param data: the element to insert
    """
    len = DL.__len__()
    if n > len + 1 or n <= 0:
        print("Insert fail: wrong position")
        return
    if n == len + 1:
        DL.add(data)
        return
    else:
        new_node = Node(data, None, None)
        if n < len/2:
            walk = DL._head
            for i in range(n - 1):
                walk = walk._next
            if n != 1:
                new_node._prev = walk._prev
                walk._prev._next = new_node
            new_node._next = walk
            walk._prev = new_node
            if n == 1:
                DL._head = new_node
        else:
            walk = DL._tail
            for i in range(len - n):
                walk = walk._prev
            new_node._prev = walk._prev
            walk._prev._next = new_node
            new_node._next = walk
            walk._prev = new_node
            if n == 1:
                DL._head = new_node
        return


def special_copy(DL1,DL2):
    """
    This function should return a new doubly linked list which contains the same element of DL1 concatenated with
    the elements of DL2 in reverse order.
     Ex. DL1 = 4 <-> 5 <-> 6, DL2 = 9 <-> 4 <-> 6 >>> returns DL3 = 4 <-> 5 <-> 6 <-> 6 <-> 4 <-> 9]
    Note: this function does not modify L1 or L2
    Note2: the method "add" of the DoublyLinkedList class adds element *at the tail* of the list
    :param DL1: a doubly linked list
    :param DL2: a doubly linked list
    """
    new = DoublyLinkedList()
    walk = DL1._head
    while walk is not None:
        new.add(walk._data)
        walk = walk._next
    walk = DL2._tail
    while walk is not None:
        new.add(walk._data)
        walk = walk._prev
    return new




""" main to do some testing"""
if __name__ == '__main__':
    """ create two doubly linked lists and add some datastore"""
    DL1 = DoublyLinkedList()
    DL2 = DoublyLinkedList()
    DL1.add("A")
    DL1.add("B")
    DL1.add("Y")
    DL1.add("Z")
    DL1.print()
    DL2.add(67)
    DL2.add(69)
    DL2.add(25)
    DL2.add(29)
    DL2.add(76)
    DL2.print()

    """ test swap """
    print("========== Test swap() ===================================")
    swap_first_with_last(DL2)
    DL2.print()
    print(str(DL2.__len__()))
    swap_first_with_last(DL2)
    DL2.print()

    """ test insert at position"""
    print("========== Test insert_at_position() ===================================")
    insert_at_position(DL2, 2, "marco")             # insert walking from head
    DL2.print()
    insert_at_position(DL2, 6, "james")             # insert walking from tail
    print(str(DL2.__len__()))
    DL2.print()
    insert_at_position(DL2, 1, "2345")              # insert at head
    DL2.print()
    insert_at_position(DL2, DL2.__len__(), "Bob")  # insert at tail
    DL2.print()
    insert_at_position(DL2, 4, "4")
    insert_at_position(DL2, 7, "7777")
    DL2.print()
    """ test cat """
    print("========== Test special_copy() ===================================")
    DL1.print()
    DL2.print()
    DL3 = special_copy(DL1, DL2)
    DL3.print()

