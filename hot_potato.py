"""
Your task is to implement 2 functions, one for simulating the classic hot potato game
and one for simulating the "spicy" version of it

==== THE HOT POTATO GAME:
In this game children line up in a circle and pass an item from neighbor to neighbor as fast as they can.
At a certain point in the game, the action is stopped and the child who has the item (the potato)
is removed from the circle. Play continues until only one child (i.e., the winner) is left.

We will implement a general simulation of the Hot Potato game:
Our program receives as input a list of names and a constant, call it “num,” to be used for counting.

To simulate the circle, we will use a queue.
Assume that the child holding the potato will be at the front of the queue.
Upon passing the potato, the simulation will simply dequeue and then immediately enqueue that child,
putting her at the end of the line. She will then wait until all the others have been at the front before it will
be her turn again. After num dequeue/enqueue operations, the child at the front will be removed permanently
(i.e., eliminated from the game) and
another cycle will begin. This process will continue until only one name remains (i.e., the size of the queue is 1).

It will return the name of the last person remaining after repetitive counting "num" times.
At each round, the program also prints the person who is eliminated


==== THE "SPICY" HOT POTATO GAME:

This time, we "spice up" the hot potato simulator by introducing (i) lives (as in videogames) and (ii) some randomness.

Like in common videogames, in this new version of the hot potato game players have "lives",
so the list of players is actually a list of list (or a matrix)
in which each player  has a name and a number of lives: e.g., ("[Marco", 7], ["Hoang", 5], ["Alice", 9])

When a round of the game ends, the loser should lose one "life". If the loser has only one life left,
then they should be eliminated. However, we also introduce "randomness" in the game...

Randomness: players do not loose a life (or get eliminated) with certainty at the end of each round.
Once a loser is determined at the end of one round, there is a 50% chance that the loser will keep their life,
and a 50% chance that they will lose it.
To simulate the 50% you can check the value of the random number generated by the
Python internal function random(), which returns a random floating point between 0 and 1 (see import statement)

ex.:
if random() > 0.5:
    # do something (e.g. keep the life)
else:
    # do something else (e.g. lose life or get eliminated)
"""
from random import random

# note this import to queue implementation in p0 package
from queue import ArrayQueue

def hot_potato(name_list, num):
    """
    Hot potato simulator. While simulating, the name of the players eliminated should also be printed
    (Note: you can print more information to see the game unfolding, for instance the list of
    players to whom the hot potato is passed at each step...)

    :param name_list: a list containing the name of the players, e.g. ["John", "James", "Alice"]
    :param num: the counting constant (i.e., the length of each round of the game)
    :return: the winner (that is, the last player standing after everybody else is eliminated)
    """
    Q = ArrayQueue()
    for i in name_list:
        Q.enqueue(i)
    
    while Q.__len__() != 1:
        for k in range(num):
            dequed = Q.dequeue()
            Q.enqueue(dequed)
        removed = Q.dequeue()
        print(f'{removed} has been removed from the game!')

    winner = Q.first()
    return winner

def hot_potato_spicy(name_list, num):
    """
    Simulates the Hot potato game "spiced up" with lives and randomness

    :param name_list: a list containing the name of the participants and their number of lives
    :param num: the counting constant (e.g., the length of each round of the game)
    :return: the winner
    """
    def oneRound():
        for k in range(num):
            dequed = Q.dequeue()
            Q.enqueue(dequed)

        if random()>0.5:
            return oneRound()
        else:
            roundLoser = Q.first()
            if lives[roundLoser] > 1:
                lives[roundLoser] -= 1
            else:
                gameLoser = Q.dequeue()
                print(f'{gameLoser} has been eliminated from the game!')

    Q = ArrayQueue()
    lives = {player[0]: player[1] for player in name_list}

    for i in name_list:
        Q.enqueue(i[0])
    
    while Q.__len__() != 1:
        oneRound()

    winner = Q.first()
    return winner


if __name__ == '__main__':
    name_list = ("Marco", "John", "Hoang", "Minji", "Hyunsuk", "Jiwoo")
    winner1 = hot_potato(name_list, 5)
    print("...and the winner in 'Hot potato' game is: {0}".format(winner1))

    name_list = (["Marco", 5], ["John", 5], ["Hoang", 5], ["Minji", 5], ["Hyunsuk", 5], ["Jiwoo", 5])
    winner2 = hot_potato_spicy(name_list, 21)
    print("...and the winner in 'Spicy hot potato' is: {0}".format(winner2))