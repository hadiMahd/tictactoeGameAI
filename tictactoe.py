"""
Tic Tac Toe Player
"""

import math,copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if terminal(board):
        return 0
    else:
        x_count=0 
        o_count=0
        for row in board:
            for cell in row:
                if cell == X:
                    x_count+=1
                elif cell == O:
                        o_count+=1

        if x_count>o_count: return O
        elif x_count==o_count: return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board): return []
    state=board
    actions=set()
    
    for r,row in enumerate(state):
            for c,cell in enumerate(row):
                if cell==EMPTY: actions.add((r,c))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    b = copy.deepcopy(board)
    r=action[0]
    c=action[1]
    "r, c = action  # Unpack the action tuple directly"
    if b[r][c] != EMPTY:
        raise ValueError("Invalid move: cell is not empty.")
    b[r][c] = player(board)
    return b



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
         if row[0]==row[1]==row[2] and row[0]!=EMPTY:
            return row[0]
    
    for col in range(3):
        if board[0][col]==board[1][col]==board[2][col] and board[0][col]!=EMPTY:
            return board[0][col]
        
    if board[0][0]==board[1][1]==board[2][2] and board[0][0]!=EMPTY:
        return board[0][0]
    if board[0][2]==board[1][1]==board[2][0] and board[0][2]!=EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)!=None: return True
    if all(cell!=EMPTY for row in board for cell in row): return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board)==X:return 1
        elif winner(board)==O:return -1
        else: return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return utility(board), None

    if player(board) == X:
        max_utility = float('-inf')
        best_move = None
        for action in actions(board):
            new_board = result(board, action)
            new_utility, _ = minimax(new_board)
            if new_utility > max_utility:
                max_utility = new_utility
                best_move = action
        return max_utility, best_move
    else:
        min_utility = float('inf')
        best_move = None
        for action in actions(board):
            new_board = result(board, action)
            new_utility, _ = minimax(new_board)
            if new_utility < min_utility:
                min_utility = new_utility
                best_move = action
        return min_utility, best_move
