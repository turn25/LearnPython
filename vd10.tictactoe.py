from __future__ import print_function
import random
import time
def drawBoard(board):
    print('===========     ===========')
    print('   |   |'+'           |   |')
    print(' '+board[1]+' | '+board[2]+' | '+board[3]+'       1 | 2 | 3')
    print('   |   |'+'           |   |')
    print('===========     ===========')
    print('   |   |'+'           |   |')
    print(' '+board[4]+' | '+board[5]+' | '+board[6]+'       4 | 5 | 6')
    print('   |   |'+'           |   |')
    print('===========     ===========')
    print('   |   |'+'           |   |')
    print(' '+board[7]+' | '+board[8]+' | '+board[9]+'       7 | 8 | 9')
    print('   |   |'+'           |   |')
    print('===========     ===========')

def inputPlayerLetter():
    letter=' '
    while not(letter=='X' or letter=='O'):
        print('Ban muon la X hay O ?')
        letter=raw_input().upper()
    if letter=='X':
        return ['X','O']
    if letter=='O':
        return ['O','X']

def whoGoesFirst():
    if random.randint(0,1) == 0:
        return 'may tinh'
    else:
        return 'nguoi choi'

def playAgain():
    print('Ban co muon choi lai ? (co/khong)')
    return raw_input().lower().startswith('c')

def makeMove(board,letter,move):
    board[move]=letter

def isWinner(board,letter):
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or
    (board[4] == letter and board[5] == letter and board[6] == letter) or
    (board[1] == letter and board[2] == letter and board[3] == letter) or
    (board[1] == letter and board[5] == letter and board[9] == letter) or
    (board[3] == letter and board[5] == letter and board[7] == letter) or
    (board[7] == letter and board[4] == letter and board[1] == letter) or
    (board[8] == letter and board[5] == letter and board[2] == letter) or
    (board[9] == letter and board[6] == letter and board[3] == letter)) 

def getBoardcopy(board):
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)
    return dupeBoard

def isSpaceFree(board,move):
    return board[move] == ' '

def getPlayerMove(board):
    move=' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board,int(move)):
        print('Ban muon di buoc nao ? (1-9)')
        move = raw_input()
    return int(move)

def ChooseRandomMoveFromList(board,movesList):
    possibleMove = []
    for i in movesList:
        if isSpaceFree(board,i):
            possibleMove.append(i)
        
    if len(possibleMove)!=0:
        return random.choice(possibleMove)
    else:
        return None

def getComputerMove(board, computerLetter):
    if computerLetter=='X':
        playerLetter='O'
    else:
        playerLetter='X'
    for i in range(1,10): #maytinh
        copy=getBoardcopy(board)
        if isSpaceFree(copy,i):
            makeMove(copy,computerLetter,i)
            if isWinner(copy,computerLetter):
                return i
    for i in range(1, 10):
        copy = getBoardcopy(board)
        if isSpaceFree(copy, i): 
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i
    move = ChooseRandomMoveFromList(board, [1,3,5,9]) #4 goc
    if move != None:
        return move
    if isSpaceFree(board,5):
        return 5
    return ChooseRandomMoveFromList(board, [2,4,6,8])

def isBoardFull(board):
    for i in range(1,10):
        if isSpaceFree(board,i):
            return False
    return True


print('Chao mung den voi TIC TAC TOE')
while True:
    Theboard=[' ']*10
    playerLetter,computerLetter= inputPlayerLetter()
    turn = whoGoesFirst()
    print('Va gio la luot cua ' + turn)
    gameisPlaying=True
    
    while gameisPlaying:
        if turn == 'nguoi choi':
            drawBoard(Theboard)
            move=getPlayerMove(Theboard)
            makeMove(Theboard, playerLetter,move)
            if isWinner(Theboard, playerLetter):
                drawBoard(Theboard)
                print('Chuc mung ban da chien thang')
                gameisPlaying=False
            else:
                if isBoardFull(Theboard):
                    drawBoard(Theboard)
                    print('Tran nay da HOA')
                    break
                else:
                    turn= 'may tinh'
        else:
            move=getComputerMove(Theboard, computerLetter)
            makeMove(Theboard, computerLetter,move)
            time.sleep(1)
            if isWinner(Theboard,playerLetter):
                drawBoard(Theboard)
                print('Ban da thua')
                gameisPlaying=False
            else:
                if isBoardFull(Theboard):
                    drawBoard(Theboard)
                    print('Tran nay HOA')
                    break
                else:
                    turn='nguoi choi'
    if not playAgain():
        break