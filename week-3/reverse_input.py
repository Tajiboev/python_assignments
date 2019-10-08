"""
    Your task is to implement
    This function reads a sequence of words provided through command line terminated by the "stop" word
    and prints them in reverse order.
    Each word is separated by the "enter", see the main() below for how to read user input from command line
    Note: this solution can be improved by (i) making sure that only 1 single words can be entered each time
    (this implementation accepts any string, including spaces) and (ii) ensuring that the last word "stop"
    is not printed....can you do it?
"""

# Do you need a stack or a queue? Import the correct datastore structure from p0 here
from stack import ArrayStack

def print_reverse_order():
    words_stack = ArrayStack()
    stop = False
    while not stop:
        word = input('Please input a word: ').strip()
        if word == 'stop':
            stop = True
            break
        words_stack.push(word)
    
    reverse = ''
    while not words_stack.is_empty():
        reverse += (f' {words_stack.pop()}')

    print(f'Your words in reverse order: {reverse.lstrip()}') 
    

if __name__ == '__main__':
    print_reverse_order()


    """
    NOTE: add some code to test your implementation of the two functions transfer and print_reverse_order
    """