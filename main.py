import math

board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '
         }

def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("\n")


def resetBoard(board):
    for key in board.keys():
        board[key] = ' '

def isFreeSpace(x):
    if board[x] == ' ':
        return True
    else:
        return False

def whoWin(mark):
    # check for rows
    if board[1] == board[2] and board[2] == board[3] and board[1] == mark:
        return True
    elif board[4] == board[5] and board[5] == board[6] and board[4] == mark:
        return True
    elif board[7] == board[8] and board[8] == board[9] and board[7] == mark:
        return True

    # check for cols
    elif board[1] == board[4] and board[4] == board[7] and board[1] == mark:
        return True
    elif board[2] == board[5] and board[5] == board[8] and board[2] == mark:
        return True
    elif board[3] == board[6] and board[6] == board[9] and board[3] == mark:
        return True

    # check for diagonals
    elif board[1] == board[5] and board[5] == board[9] and board[1] == mark:
        return True
    elif board[3] == board[5] and board[5] == board[7] and board[3] == mark:
        return True

    else:
        return False

def drawGame():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True

def insert(symbol, position):
    if isFreeSpace(position):
        board[position] = symbol
        printBoard(board)

        if drawGame():
            print("Draw!")
            playAgain = input("Would you like to play again? y/n \n")
            if playAgain == 'y' or playAgain == "Yes" or playAgain == "YES" or playAgain == 'Y':
                resetBoard(board)
                playerMove()
            else:
                exit()


        if whoWin(player):
            print("Player wins!")
            playAgain = input("Would you like to play again? y/n")
            if playAgain == 'y' or playAgain == "Yes" or playAgain == "YES" or playAgain == 'Y':
                resetBoard(board)
                playerMove()
            else:
                exit()

        elif whoWin(computer):
            print("Computer wins!")
            playAgain = input("Would you like to play again? y/n")
            if playAgain == 'y' or playAgain == "Yes" or playAgain == "YES" or playAgain == 'Y':
                resetBoard(board)
                playerMove()
            else:
                exit()
        return

    else:
        print("Space is taken!")
        position = int(input("Enter new position: "))
        insert(symbol, position)
        return

player = 'X'
computer = 'O'

def playerMove():
    pos = input("Choose a position for 'X' (from 1 - 9): ")
    if(pos == '1' or pos == '2' or pos == '3'
            or pos == '4' or pos == '5' or pos == '6' or pos == '7'
            or pos == '8' or pos == '9'):
        pos_int = int(pos)
        insert(player, pos_int)
        computerMove()
        return
    else:
        print("Invalid input, please choose from 1 - 9")
        playerMove()

def computerMove():
    bestScore = -1000
    bestMove = 0
#   check all empty spot in the board
    for key in board.keys():
        if board[key] == ' ':
            board[key] = computer
            score = minimax(board, 0, False)
            # undo the insert
            board[key] = ' '
            if bestScore < score:
                bestScore = score
                bestMove = key

    insert(computer, bestMove)

def minimax(board, depth, isMaximizing):
    if whoWin(player):
        return -1
    elif whoWin(computer):
        return 1
    elif drawGame():
        return 0

    if isMaximizing:
        bestScore = -1000
        #   check all empty spot in the board
        for key in board.keys():
            if board[key] == ' ':
                board[key] = computer
                score = minimax(board, 0, False)
                # undo the insert
                board[key] = ' '
                bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = 1000
        #   check all empty spot in the board
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                score = minimax(board, 0, True)
                # undo the insert
                board[key] = ' '
                bestScore = min(score, bestScore)
        return bestScore


def playGame():
    printBoard(board)
    while not (whoWin(player) or whoWin(computer)):
        playerMove()

playGame()