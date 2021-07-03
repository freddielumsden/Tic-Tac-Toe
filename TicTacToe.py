board = [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]
turn = 'X'
draw = False
def printBoard():
    print("     |     |     ")
    print("  {}  |  {}  |  {}  ".format(board[0][0], board[0][1], board[0][2]))
    print("_____|_____|_____")
    print("     |     |     ")
    print("  {}  |  {}  |  {}  ".format(board[1][0], board[1][1], board[1][2]))
    print("_____|_____|_____")
    print("     |     |     ")
    print("  {}  |  {}  |  {}  ".format(board[2][0], board[2][1], board[2][2]))
    print("     |     |     ")
print("Welcome to tic tac toe!\n\n")
while True:
    printBoard()
    print("It is " + turn + "'s go.")
    while True:
        try:
            position = int(input("Pick your position on the board by choosing an integer between 1 and 9: "))
            if position < 1 or position > 9:
                raise TypeError()
            if position == 1:
                if board[0][0] == ' ':
                    board[0][0] = turn
                else:
                    raise TypeError()
            if position == 2:
                if board[0][1] == ' ':
                    board[0][1] = turn
                else:
                    raise TypeError()
            if position == 3:
                if board[0][2] == ' ':
                    board[0][2] = turn
                else:
                    raise TypeError()
            if position == 4:
                if board[1][0] == ' ':
                    board[1][0] = turn
                else:
                    raise TypeError()
            if position == 5:
                if board[1][1] == ' ':
                    board[1][1] = turn
                else:
                    raise TypeError()
            if position == 6:
                if board[1][2] == ' ':
                    board[1][2] = turn
                else:
                    raise TypeError()
            if position == 7:
                if board[2][0] == ' ':
                    board[2][0] = turn
                else:
                    raise TypeError()
            if position == 8:
                if board[2][1] == ' ':
                    board[2][1] = turn
                else:
                    raise TypeError()
            if position == 9:
                if board[2][2] == ' ':
                    board[2][2] = turn
                else:
                    raise TypeError()
            break
        except:
            print("Please input a valid number.")
    if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':
        printBoard()
        print("\n\nX Wins!\n\n")
        break
    elif board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
        printBoard()
        print("\n\nX Wins!\n\n")
        break
    elif board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
        printBoard()
        print("\n\nX Wins!\n\n")
        break
    elif board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
        printBoard()
        print("\n\nX Wins!\n\n")
        break
    elif board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
        printBoard()
        print("\n\nX Wins!\n\n")
        break
    elif board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
        printBoard()
        print("\n\nX Wins!\n\n")
        break
    elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        printBoard()
        print("\n\nX Wins!\n\n")
        break
    elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        printBoard()
        print("\n\nX Wins!\n\n")
        break


    if board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O':
        printBoard()
        print("\n\nO Wins!\n\n")
        break
    elif board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O':
        printBoard()
        print("\n\nO Wins!\n\n")
        break
    elif board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O':
        printBoard()
        print("\n\nO Wins!\n\n")
        break
    elif board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':
        printBoard()
        print("\n\nO Wins!\n\n")
        break
    elif board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O':
        printBoard()
        print("\n\nO Wins!\n\n")
        break
    elif board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
        printBoard()
        print("\n\nO Wins!\n\n")
        break
    elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        printBoard()
        print("\n\nO Wins!\n\n")
        break
    elif board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        printBoard()
        print("\n\nO Wins!\n\n")
        break

    if board[0][0] != ' ' and board[0][1] != ' ' and board[0][2] != ' ' and board[1][0] != ' ' and board[1][1] != ' ' and board[1][2] != ' ' and board[2][0] != ' ' and board[2][1] != ' ' and board[2][2] != ' ':
        print("\n\nIt's a draw!\n\n")
        break


    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'