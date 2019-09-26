"""
Your task is to
implement a function intersection(A,B,C) that
tests whether the intersection of the lists A, B, and C is empty
Assuming that the 3 lists have at most 1 element in common, in case of
not empty intersection the function prints the positions in the 3 lists at
which the common element is found.
Example:
A = [4, 7, 8, 4], B=[89, 76], C=[6,9,67]
(no intersection)

A = [4, 7, 8, 4], B=[9, 1, 7, 3, 4], C=[56, 33, 7]
intersection(A,B,C) prints the message
Intersection found at A[1], B[2], C[2]

Your solution should also print the time it took to execute the function
Note the import of the function "time" to capture the current time in your program
More info about importing modules: https://en.wikibooks.org/wiki/A_Beginner%27s_Python_Tutorial/Importing_Modules

Once you have completed your implementation, answer the following question:
What is the time complexity of your solution?
What about the worst case?
"""
from time import time

# use time() to capture the current system time in your code, e.g., start_time = time()

def intersection_slow(A,B,C):
    """
    sleep() calls are delays of 0.3s
    introduced to make you appreciate the compelxity of the the 2 solution
    (this and slow below)
    """
    # O(n^3)
    result = []
    for i in A:
        for j in B:
            for k in C:
                if k == j and j == i:
                    result.append(k)
    return result
                
    

def intersection_fast(A,B,C):
    """
    sleep() calls are delays of 0.3s
    introduced to make you appreciate the compelxity of the the 2 solution
    (this and slow below)
    """

    # O(n^2)
    result = []
    for i in A:
        for j in B:
            if i == j:
                for k in C:
                    if k == j:
                        result.append(k)
    return result
    



if __name__ == '__main__':
    A = [4, 7, 8, 4]
    B = [89, 76]
    C = [6, 9, 67]
    print(intersection_slow(A,B,C))



    D = [4, 7, 8, 4]
    E = [9, 1, 7, 3, 4]
    F = [56, 33, 7]
    print(intersection_fast(D,E,F))



