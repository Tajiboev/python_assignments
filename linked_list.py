class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def append(self, data):
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

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert_at_position(self, position, data):
        if position < 1 or position > self.length + 1:
            print(f'Insertion error, invalid position: {position}')
            return
       
        new_node = Node(data)
        
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

        if position > 1:
            current_node = self.head
            node_count = 2
            while node_count < position:
                current_node = current_node.next
                node_count += 1       
            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1

    # deletion operations

    def delete_nth(self, position):
        if position < 1 or position > self.length:
            print(f'Deletion error, invalid position: {position}')
            return

        if position == 1:
            current_node = self.head
            self.head = current_node.next
            current_node = None
            self.length -= 1
            return

        current_node = self.head
        node_count = 2
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
            self.delete_nth(1)
            return
        
        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next
        
        if current_node is None:
            return 'Element is not in the list'
        
        prev.next = current_node.next
        current_node = None
        self.length -= 1


llist = LinkedList()
llist.append('A')
llist.append('B')
llist.insert_at_position(2, "M")
llist.insert_at_position(3, "U")
llist.insert_at_position(4, "H")
llist.delete_nth(1)
llist.delete_node('B')
llist.prepend('S')
llist.delete_node('!')
llist.print_list()
print(llist.length)