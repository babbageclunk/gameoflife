WIDTH = 10
HEIGHT = 10

def main():
    """
    GO
    """
    board = [[[] for x in xrange(HEIGHT)] for x in xrange(WIDTH)]
    for row in board:
        print row


if __name__ == '__main__':
    main()
