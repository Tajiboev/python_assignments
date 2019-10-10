"""
Note that this implementation of the linked list is simpler and, therefore, slightly
different from the one in the GTG book.
"""

class Node:
    """Lightweight, nonpublic class for storing a singly linked node."""

    def __init__(self, element):
        self._data = element
        self._next = None


class LinkedList:
    def __init__(self):
        self._head = None

    def __len__(self):
        current = self._head
        if current is None:
            return 'List is empty'
        
        count = 0
        while current:
            count += 1
            current = current._next
        return count

    
    def append(self, data):
        new_node = Node(data)

        if self._head is None:
            self._head = new_node
            return
        
        last_node = self._head
        while last_node._next:
            last_node = last_node._next
        last_node._next = new_node


    def add_first(self, e):
        """ ad an element at the start of the list (i.e., after the "head" """
        temp = Node(e)
        temp._next = self._head
        self._head = temp
    
    def add_last(self, e):
        """ ad an element at the start of the list (i.e., after the "head" """
        temp = Node(e)
        if self._head is None:
            self._head = temp
        
        last_node = self._head
        while last_node._next:
            last_node = last_node._next
        last_node._next = temp


    def remove_first(self):
        if self._head is None:
            print("Cannot remove, list is empty")
        else:
            self._head = self._head._next

    def print(self):
        current = self._head
        while current._next is not None:
            print(current._data, end=" ")
            current = current._next
        print(current._data, end="\n")

    # does not work if e is not in the list
    def find_and_remove(self, e):
        current = self._head
        previous = None
        stop_loop = False
        in_list = False
        while not stop_loop:
            # if end of the list
            if current == None:
                print("Element {0} not found in list".format(e))
                stop_loop = True  # to stop the while loop!
            elif current._data == e:
                print("Element {0} found in list....removed".format(e))
                stop_loop = True
                in_list = True
            else:
                previous = current
                current = current._next

        if in_list:
            if previous == None:
                self._head = current._next
            else:
                previous._next = current._next

    """ this can be done as homework!!!
    remove an element at position n"""

    def remove_at_position(self, position):
        if position == 0:
            current_node = self._head
            self._head = current_node._next
            current_node = None
            return

        current_node = self._head
        node_count = 1
        while node_count < position:
            current_node = current_node._next
            node_count += 1
        next_node = current_node._next
        current_node._next = next_node._next
        next_node = None


    def insert_at_position(self, position, data):
        new_node = Node(data)
        
        if position == 0:
            new_node._next = self._head
            self._head = new_node

        if position > 0:
            current_node = self._head
            node_count = 1
            while node_count < position:
                current_node = current_node._next
                node_count += 1       
            new_node._next = current_node._next
            current_node._next = new_node

if __name__ == '__main__':
    list = LinkedList()
    list.add_first(100)
    list.add_first(34)
    list.add_first(87)
    list.add_last(150)
    list.add_last(2000)
    list.print()
    list.find_and_remove(87)
    list.find_and_remove("Marco")
    list.add_first("Marco")
    list.print()
    list.remove_at_position(3)
    list.print()
    list.remove_at_position(0)
    list.print()
    list.add_last(140)
    list.add_first("Marco")                     # note that I can add anything to a list
    list.add_first("John")
    list.add_last(67)
    list.insert_at_position(1, "work")
    list.remove_at_position(2)
    list.print()
    print(list.__len__())