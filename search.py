from game import *

# Search routines use negamax simplification, see: http://en.wikipedia.org/wiki/Negamax

# Number of states expanded during negamax search
nm_st_exp = 0

def negamax(game, heur_fn, state, depth, color, trace=0):
    '''negamax algorithm, a simplification of the standard minimax but with the player
       represented by the color parameter (which is either 1 for first player, -1 for second)
    input:
       game is the Game object 
       state is the state we are evaluating
       depth is the depth in the search
       color determines which player turn it is {1,-1}
    output:
       the highest heuristic value player 'color' can get from any action
    '''
    global nm_st_exp
    nm_st_exp += 1

    if trace > 1:
        game.print_state(state)
        print("")

    # If we're at depth limit or terminal node, return heuristic value
    if game.terminal(state) or (depth == 0):
        return color * heur_fn.heuristic(game, state)

    # Find the next move with the best heuristic value
    best_val = heur_fn.get_lower_bound()
    moves = game.moves(color, state)

    for m in moves:
        child = game.next_state(color, state, m)
        val = -negamax(game, heur_fn, child, depth - 1, -color, trace)
        best_val = max(best_val, val)

    return best_val

def negamax_ab(game, heur_fn, state, depth, alpha, beta, color, trace=0):
    '''negamax algorithm with alpha-beta pruning'''
    global nm_st_exp
    nm_st_exp += 1

    if trace > 1:
        game.print_state(state)
        print("")

    # If we're at depth limit or terminal node, return heuristic value
    if game.terminal(state) or (depth == 0):
        return color * heur_fn.heuristic(game, state)

    # Find the next move with the best heuristic value, stopping early if necessary
    best_val = heur_fn.get_lower_bound()
    moves = game.moves(color, state)

    for m in moves:
        child = game.next_state(color, state, m)
        val = -negamax_ab(game, heur_fn, child, depth - 1, -beta, -alpha, -color, trace)
        best_val = max(best_val, val)
        alpha = max(alpha, val)
        if alpha >= beta:
            break
    return best_val
