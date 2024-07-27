###############################################################################
# This file implements various minimax search agents.
#
# CSC 384 Fall 2023 Assignment 2
# version 1.0
###############################################################################
from mancala_game import Board, play_move
from utils import *

def check_terminal(board):
    result = 0;
    for i in board.pockets:
        for j in i:
            if j != 0:
                result += 1;
                break;
    return 0 if result == 2 else 1
def result(board, index, curr_player):
    num_of_stones = board.pockets[curr_player][index]
    board.pockets[curr_player][index] = 0
    #player = curr_player
    delta = 1
    while num_of_stones > 0:
        if curr_player == BOTTOM:
            index += delta
            if index <= 5:
                board.pockets[curr_player][index] += 1
                num_of_stones -= 1
            elif index == 6:
                board.mancalas[curr_player] += 1
                curr_player = TOP
                num_of_stones -= 1
                delta = -delta
            else:
                print("Exception Case")
        else:
            index += delta
            if index >= 0:
                board.pockets[curr_player][index] += 1
                num_of_stones -= 1
            elif index == -1:
                delta = -delta
                curr_player = BOTTOM
    return board

def minimax_max_basic(board, curr_player, heuristic_func):
    """
    Perform Minimax Search for MAX player.
    Return the best move and its minimax value.
    If the board is a terminal state, return None as its best move.

    :param board: the current board
    :param curr_player: the current player
    :param heuristic_func: the heuristic function
    :return the best move and its minimax value according to minimax search.
    """
    opponent = BOTTOM
    if curr_player == BOTTOM:
        opponent = TOP
    else:
        opponent = BOTTOM
    if check_terminal(board) :
        return None, heuristic_func(board, curr_player)
    best_move = None
    best_value = -100000
    for move in board.get_possible_moves(curr_player):
        pockets = [[0] * len(board.pockets[0]) for _ in range(2)]
        #pockets = board.pockets
        for i in range(2):
            for j in range(len(board.pockets[0])):
                pockets[i][j] = board.pockets[i][j]
        mancalas = [0, 0]
        for i in range(2):
            mancalas[i] = board.mancalas[i]
        #mancalas = board.mancalas
        temp = Board(pockets, mancalas)
        next_state = play_move(temp, curr_player, move)
        _,value = minimax_min_basic(next_state, opponent, heuristic_func)
        if value > best_value:
            best_move = move
            best_value = value

    return best_move, best_value
    #raise NotImplementedError


def minimax_min_basic(board, curr_player, heuristic_func):
    """
    Perform Minimax Search for MIN player.
    Return the best move and its minimax value.
    If the board is a terminal state, return None as its best move.

    :param board: the current board
    :param curr_player: the ccurrent player
    :param heuristic_func: the heuristic function
    :return the best move and its minimax value according to minimax search.
    """
    opponent = BOTTOM
    if curr_player == BOTTOM:
        opponent = TOP
    else:
        opponent = BOTTOM
    if check_terminal(board) :
        return None, heuristic_func(board, opponent)
    best_move = None
    best_value = 100000
    for move in board.get_possible_moves(curr_player):
        pockets = [[0] * len(board.pockets[0]) for _ in range(2)]
        #pockets = board.pockets
        for i in range(2):
            for j in range(len(board.pockets[0])):
                pockets[i][j] = board.pockets[i][j]
        mancalas = [0,0]
        #mancalas = board.mancalas
        for i in range(2):
            mancalas[i] = board.mancalas[i]

        temp = Board(pockets, mancalas)
        next_state = play_move(temp, curr_player, move)
        
        _, value = minimax_max_basic(next_state, opponent, heuristic_func)
        if value < best_value:
            best_move = move
            best_value = value

    return best_move, best_value

    #raise NotImplementedError


def minimax_max_limit(board, curr_player, heuristic_func, depth_limit):
    """
    Perform Minimax Search for MAX player up to the given depth limit.
    Return the best move and its estimated minimax value.
    If the board is a terminal state, return None as its best move.

    :param board: the current board
    :param curr_player: the current player
    :param heuristic_func: the heuristic function
    :param depth_limit: the depth limit
    :return the best move and its minimmax value estimated by our heuristic function.
    """
    opponent = BOTTOM
    if curr_player == BOTTOM:
        opponent = TOP
    else:
        opponent = BOTTOM
    if check_terminal(board) or depth_limit == 0:
        return None, heuristic_func(board, curr_player)
    best_move = None
    best_value = -100000
    for move in board.get_possible_moves(curr_player):
        pockets = [[0] * len(board.pockets[0]) for _ in range(2)]
        #pockets = board.pockets
        for i in range(2):
            for j in range(len(board.pockets[0])):
                pockets[i][j] = board.pockets[i][j]
        mancalas = [0, 0]
        for i in range(2):
            mancalas[i] = board.mancalas[i]
        #mancalas = board.mancalas
        temp = Board(pockets, mancalas)
        next_state = play_move(temp, curr_player, move)
        _,value = minimax_min_limit(next_state, opponent, heuristic_func, depth_limit - 1)
        if value > best_value:
            best_move = move
            best_value = value

    return best_move, best_value

    #raise NotImplementedError

def minimax_min_limit(board, curr_player, heuristic_func, depth_limit):
    """
    Perform Minimax Search for MIN player  up to the given depth limit.
    Return the best move and its estimated minimax value.
    If the board is a terminal state, return None as its best move.

    :param board: the current board
    :param curr_player: the ccurrent player
    :param heuristic_func: the heuristic function
    :param depth_limit: the depth limit
    :return the best move and its minimmax value estimated by our heuristic function.
    """
    opponent = BOTTOM
    if curr_player == BOTTOM:
        opponent = TOP
    else:
        opponent = BOTTOM
    if check_terminal(board) or depth_limit == 0:
        return None, heuristic_func(board, opponent)
    best_move = None
    best_value = 100000
    for move in board.get_possible_moves(curr_player):
        pockets = [[0] * len(board.pockets[0]) for _ in range(2)]
        #pockets = board.pockets
        for i in range(2):
            for j in range(len(board.pockets[0])):
                pockets[i][j] = board.pockets[i][j]
        mancalas = [0,0]
        #mancalas = board.mancalas
        for i in range(2):
            mancalas[i] = board.mancalas[i]

        temp = Board(pockets, mancalas)
        next_state = play_move(temp, curr_player, move)

        _, value = minimax_max_limit(next_state, opponent, heuristic_func, depth_limit - 1)
        if value < best_value:
            best_move = move
            best_value = value

    return best_move, best_value

    #raise NotImplementedError

'''def cache_exist(board, cache, curr_player):
    for key, data in cache:
        if key.pockets != board.pockets or key.mancalas != board.mancalas or data[2] != curr_player:
            continue;
        return data[0], data[1]
    return -1, -1

'''
def minimax_max_limit_caching(board, curr_player, heuristic_func, depth_limit, cache):
    """
    Perform Minimax Search for MAX player up to the given depth limit with the option of caching states.
    Return the best move and its minimmax value estimated by our heuristic function.
    If the board is a terminal state, return None as its best move.

    :param board: the current board
    :param curr_player: the ccurrent player
    :param heuristic_func: the heuristic function
    :param depth_limit: the depth limit
    :param caching: whether we are caching states.
    :return the best move and its minimmax value estimated by our heuristic function.
    """
    opponent = BOTTOM
    if curr_player == BOTTOM:
        opponent = TOP
    else:
        opponent = BOTTOM
    if check_terminal(board) or depth_limit == 0:
        return None, heuristic_func(board, curr_player)
    
    best_move = None
    best_value = -100000
    for move in board.get_possible_moves(curr_player):
        pockets = [[0] * len(board.pockets[0]) for _ in range(2)]
        #pockets = board.pockets
        for i in range(2):
            for j in range(len(board.pockets[0])):
                pockets[i][j] = board.pockets[i][j]
        mancalas = [0, 0]
        for i in range(2):
            mancalas[i] = board.mancalas[i]
        #mancalas = board.mancalas
        temp = Board(pockets, mancalas)
        next_state = play_move(temp, curr_player, move)
        if next_state in cache:
            val, dep, ply = cache[next_state]
            if dep >= depth_limit - 1 and ply == opponent:
                value = val
            else:
                _,value = minimax_min_limit_caching(next_state, opponent, heuristic_func, depth_limit - 1, cache)
        else:
            _,value = minimax_min_limit_caching(next_state, opponent, heuristic_func, depth_limit - 1, cache)
        if value > best_value:
            best_move = move
            best_value = value

    if board in cache:
        val, dep, ply = cache[board]
        if ply == curr_player and dep > depth_limit:
            pass
        else:
            cache[board] = [best_value, depth_limit, curr_player]
    else:
        cache[board] = [best_value, depth_limit, curr_player]


    return best_move, best_value
    
    #raise NotImplementedError


def minimax_min_limit_caching(board, curr_player, heuristic_func, depth_limit, cache):
    """
    Perform Minimax Search for MIN player up to the given depth limit with the option of caching states.
    Return the best move and its minimmax value estimated by our heuristic function.
    If the board is a terminal state, return None as its best move.

    :param board: the current board
    :param curr_player: the current player
    :param heuristic_func: the heuristic function
    :param depth_limit: the depth limit
    :param caching: whether we are caching states.
    :return the best move and its minimmax value estimated by our heuristic function.
    """
    opponent = BOTTOM
    if curr_player == BOTTOM:
        opponent = TOP
    else:
        opponent = BOTTOM
    if check_terminal(board) or depth_limit == 0:
        #cache[board] = heuristic_func(board, opponent)
        #val, dep = cache_exist(board, cache, curr_player)
        
        #if dep == -1:
        #    cache[board] = [heuristic_func(board, opponent), depth_limit, curr_player]
        return None, heuristic_func(board, opponent)
    
    best_move = None
    best_value = 100000
     
    for move in board.get_possible_moves(curr_player):
      
        
        pockets = [[0] * len(board.pockets[0]) for _ in range(2)]
        #pockets = board.pockets
        for i in range(2):
            for j in range(len(board.pockets[0])):
                pockets[i][j] = board.pockets[i][j]
        mancalas = [0,0]
        #mancalas = board.mancalas
        for i in range(2):
            mancalas[i] = board.mancalas[i]

        temp = Board(pockets, mancalas)
        next_state = play_move(temp, curr_player, move)
        if next_state in cache:
            val, dep, ply = cache[next_state]
            if dep >= depth_limit - 1 and ply == opponent:
                value = val
            else:
                _, value = minimax_max_limit_caching(next_state, opponent, heuristic_func, depth_limit - 1, cache)
        else:
            _, value = minimax_max_limit_caching(next_state, opponent, heuristic_func, depth_limit - 1, cache)
        if value < best_value:
            best_move = move
            best_value = value
    
    if board in cache:
        val, dep, ply = cache[board]
        if ply == curr_player and dep > depth_limit:
            pass
        else:
            cache[board] = [best_value, depth_limit, curr_player]
    else:
        cache[board] = [best_value, depth_limit, curr_player]

    return best_move, best_value

    #raise NotImplementedError


###############################################################################
## DO NOT MODIFY THE CODE BELOW.
###############################################################################

def run_ai():
    """
    This function establishes communication with the game manager.
    It first introduces itself and receives its color.
    Then it repeatedly receives the current score and current board state
    until the game is over.
    """
    print("Mancala AI")  # First line is the name of this AI
    arguments = input().split(",")

    player = int(arguments[0])  # Player color
    limit = int(arguments[1])  # Depth limit
    caching = int(arguments[2])  # Caching
    hfunc = int(arguments[3]) # Heuristic Function

    if (caching == 1): 
        caching = True
    else: 
        caching = False

    eprint("Running MINIMAX")


    if limit == -1:
        eprint("Depth Limit is OFF")
    else:
        eprint("Depth Limit is", limit)

    if caching:
        eprint("Caching is ON")
        cache = {}
    else:
        eprint("Caching is OFF")

    if hfunc == 0:
        eprint("Using heuristic_basic")
        heuristic_func = heuristic_basic
    else:
        eprint("Using heuristic_advanced")
        heuristic_func = heuristic_advanced

    while True:  # This is the main loop
        # Read in the current game status, for example:
        # "SCORE 2 2" or "FINAL 33 31" if the game is over.
        # The first number is the score for player 1 (dark), the second for player 2 (light)
        next_input = input()
        status, dark_score_s, light_score_s = next_input.strip().split()

        if status == "FINAL":  # Game is over.
            print()
        else:
            pockets = eval(input())  # Read in the input and turn it into an object
            mancalas = eval(input())  # Read in the input and turn it into an object
            board = Board(pockets, mancalas)

            # Select the move and send it to the manager
            if caching:
                move, value = minimax_max_limit_caching(board, player, heuristic_func, limit, cache)
            elif limit >= 0:
                move, value = minimax_max_limit(board, player, heuristic_func, limit)
            else:
                move, value = minimax_max_basic(board, player, heuristic_func)
            print("{}".format(move))


if __name__ == "__main__":
    run_ai()
