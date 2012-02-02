WIDTH = 10
HEIGHT = 10

import random

def main():
    """
    GO
    """
    board = [[random.choice('x ') for x in xrange(HEIGHT)] for x in xrange(WIDTH)]
    for row in board:
        print row

def neighbours(x, y):
    for dx in range(-1, 2):
        for dy in range (-1, 2):
            if dy == dx == 0:
                continue
            yield x + dx, y + dy

# Any live cell with fewer than two live neighbours dies, as if caused by under-population.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overcrowding.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

def is_alive(x, y, board):
    live_n = 0
    for nx, ny in neighbours(x, y):
        live_n += 1 if board[y % HEIGHT][x % WIDTH] else 0
    if live_n < 2:
        return False
    elif live_n == 3:
        return True
    elif 2 <= live_n <= 3:
        return board[y][x]
    else:
        return False



def tick(board):
    new_board = []
    for y in range(HEIGHT):
        row = []
        for x in range(WIDTH):
            row.append(is_alive(x, y, board))
        new_board.append(row)
    return new_board

if __name__ == '__main__':
    main()
