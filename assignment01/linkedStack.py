class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class LinkedStack:
    """LIFO Stack implementation using linked-list as underlying storage."""

    def __init__(self):
        """Create an empty stack."""
        self.head = None

    def is_empty(self):
        """Return True if the stack is empty."""
        return self.head == None

    def push(self, data):
        """Add new element to the top of the stack."""
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
 
    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise AssertionError('Stack is empty')
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped
    
    def top(self):
        """Return (but do not remove) the element at the top of the stack. --> Node(data)

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise AssertionError('Stack is empty')
        
        return self.head


    def print_content(self):
        if self.head is None:
            raise AssertionError('Stack is empty')
        
        stack_as_list = []
        current = self.head
        while current:
            stack_as_list.append(current.data)
            current = current.next
        stack_as_list.reverse()
        print(f'"Stack content: {stack_as_list}"')