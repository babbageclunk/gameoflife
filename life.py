import os
import random
import time
import colorama
import sys

from colorama import init, Back
init()

WIDTH = 40
HEIGHT = 180 # Not really



def printer(board):
    """
    Print a board

    Arguments:
    - `board`:
    """
    os.system("clear")
    print "-" * HEIGHT
    for row in board:
        sys.stdout.write("|")
        for cell in row:
            if cell:
                sys.stdout.write(Back.RED + "*" + Back.RESET)
            else:
                sys.stdout.write(" ")
        sys.stdout.write("|\n")
    print "-" * HEIGHT

def create_board():
    """
    Create a random board
    """
    board = [[None for x in xrange(HEIGHT)] for x in xrange(WIDTH)]
    for row in board:
        for i, cell  in enumerate(row):
            if i % random.randint(1, 10) == 0:
                row[i] = True
    return board


def life():
    """
    The game of life
    """
    printer(create_board())


def main():
    """
    GO
    """
    while True:
        life()
        time.sleep(0.5)
        print "Thinking....."
        time.sleep(random.randint(1, 3))

if __name__ == '__main__':
    main()
