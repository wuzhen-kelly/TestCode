#Tic-Tac-Toe
#跟人类对手下井字棋

#全局变量
X="X"
O="O"
EMPTY=""
TIE="TIE"
NUM_SQUARES=9

#显示游戏的说明
def instructions():
    """Display game instructions."""
    print(
    """
    Welcome to the greatest intellectual challenge of all time :Tic-Tac-Toe.
    This will be a showdown between your human brain and my silicon processor.
    You will make your move know by entering a number,0-8.The number
    will correspond to the board position as illustrated:
                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 |8
    Prepare yourself ,human.The ultimate battle is about to begin.\n
    """
    )

def ask_yes_no(question):
    """Ask a yes or no question."""
    response=None
    while response not in('y',"n"):
        response=input(question).lower()
    return response

#用于请求用户给出指定范围内的一个数字
def ask_number(question,low,high):
    """Ask for a number within a range."""
    response=None
    while response not in range(low,high):
        response=int(input(question))
    return response

#询问玩家是否希望先行棋，然后据此返回机器人和玩家的棋子。跟进井字棋的传统玩法，X先走

def pieces():
    """Determine if player or computer goes first."""
    go_first=ask_yes_no("Do you require the first move?(y/n):")
    if go_first=="y":
        print("\nThen take the first move.You will need it.")
        human=X
        computer=O
    else:
        print("\nYour bravery will be your undoing...I will go first.")
        computer=X
        human=O
    return computer,human

#用于创建新棋盘（一个长度为9的列表，各元素均被设置为EMPTY），然后将其返回
def new_board():
    """Create new game board."""
    board=[]
    for suqare in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

#将棋盘显示出来
def display_board(board):
    """Display game board on screen."""
    print("\n\t",board[0],"|",board[1],"|"board[2])
    print(""\t,"---------")
    print("\n\t",board[3],"|",board[4],"|"board[5])
    print(""\t,"---------")
    print("\n\t",board[6],"|",board[7],"|"board[8],"\n")

#该函数接收一个棋盘，并返回一组合法的行棋步骤
def legal_move(board):

