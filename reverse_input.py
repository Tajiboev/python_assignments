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
# from m03_sequences.p0.stack import ???

def print_reverse_order():

    pass

if __name__ == '__main__':
    """
    Run this to understand how to read user input from command line
    """
    print("Enter one word: ")
    word1 = input()
    print("You entered: {0}".format(word1))
    print("---- Read a sequence of words ---")
    word = " "
    stop = False
    while not stop:
        word = input()
        print("You entered: {0}".format(word))
        if word == "stop":
            print("STOP!")

    """
    NOTE: add some code to test your implementation of the two functions transfer and print_reverse_order
    """