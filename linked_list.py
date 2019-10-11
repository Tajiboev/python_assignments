class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def is_empty(self):
        return self.length == 0

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def add_last(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.length += 1
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        self.length += 1

    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert_at_position(self, position, data):
        if position < 0 or position > self.length + 1:
            raise ValueError(f'Insertion error, invalid position: {position}')
        
        if position == 0:
            self.add_first(data)

        if position > 0:
            new_node = Node(data)
            current_node = self.head
            node_count = 1
            while node_count < position:
                current_node = current_node.next
                node_count += 1       
            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1

    #finding element
    def position_of_element(self, element):
        if self.is_empty():
            return "The list is empty"
        
        current = self.head
        count = 0
        while current and current.data != element:
            current = current.next
            count += 1
        
        if current is None:
            return "The element is not in the list"
        else:
            return count
    
    def element_at_position(self, position):
        if position > self.length - 1 or position < 0:
            raise ValueError("Invalid position")

        if self.is_empty():
            return "The list is empty"

        current, count = self.head, 0
        
        while count != position:
            current = current.next
            count += 1
        
        return current.data


    # deletion operations

    def delete_nth(self, position):
        if position < 0 or position > self.length:
            raise ValueError(f'Deletion error, invalid position: {position}')

        if position == 0:
            current_node = self.head
            self.head = current_node.next
            current_node = None
            self.length -= 1
            return

        current_node = self.head
        node_count = 1
        while node_count < position:
            current_node = current_node.next
            node_count += 1
        next_node = current_node.next
        current_node.next = next_node.next
        next_node = None
        self.length -= 1

    def delete_node(self, key):
        current_node = self.head
        
        if current_node and current_node.data == key:
            return self.delete_nth(0)
        
        previous = None
        while current_node and current_node.data != key:
            previous = current_node
            current_node = current_node.next
        
        if current_node is None:
            return "Element not found in the list"
        else:
            previous.next = current_node.next
            current_node = None
            self.length -= 1



llist = LinkedList()
llist.add_last('A')
llist.add_first('B')
llist.insert_at_position(2, "M")
llist.element_at_position(2) #returns M
llist.delete_nth(1)
llist.delete_node('M')
llist.print_list()
print(llist.length)