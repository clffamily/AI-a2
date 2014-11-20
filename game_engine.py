import time

from game import *
import search

class GameEngine:
    '''GameEngine class encapsulates an interface to the user and search procedures.'''

    def __init__(self, max_depth, trace=0):
        '''Initializes the game engine.
        input:
           max_depth determines the maximum depth reached during search.
           trace is 2 for max debug output, 1 for debug output, 0 otherwise
        '''
        self.max_depth = max_depth
        self.trace = trace

    def player_move(self, game, state, color):
        '''Returns the state that results from the player's chosen action.
        input:
           game is the Game object
           state is the current game state
           color is the player's color {-1,1}
        output is the state that results from following the player's action
        '''
        # Get player input
        while 1:
            player_inp = input('Enter move: ')
            player_move = game.parse_player_move(player_inp)
            if game.valid_move(state, player_move):
                break
            print("Incorrect input.")

        # Return resulting state
        return game.next_state(color, state, player_move)

    def computer_move(self, game, heur_fn, state, color, ab_enable):
        '''Returns the state that results from the computer's chosen action.
        input:
           game is the Game object
           heur_fn is a Heuristic object that encapsulates the heuristic function
           state is the current game state
           color is the player's color {-1,1}
           ab_enable determines whether we use alpha-beta pruning in the search
        output is the state that results from following the computer's action
        '''
        max_state = None
        max_val = heur_fn.get_lower_bound()

        # Get the move whose resulting state has the highest heuristic value
        moves = game.moves(color, state)
        for m in moves:
            next_state = game.next_state(color, state, m)

            if ab_enable:
                val = -search.negamax_ab(game, heur_fn, next_state, self.max_depth, heur_fn.get_lower_bound(), heur_fn.get_upper_bound(), -color, self.trace)
            else:
                val = -search.negamax(game, heur_fn, next_state, self.max_depth, -color, self.trace)

            if max_val < val:
                max_val = val
                max_state = next_state

        return max_state

    def reset_stats(self):
        '''Resets search statistics.'''
        # Reset states expanded during negamax search
        search.nm_st_exp = 0
        self.total_search_time = time.time()

    def play(self, game, heur_fn, ab_enable=False, player_first=True):
        '''User plays against the computer.
        input:
           game is the Game object
           heur_fn is a Heuristic object that encapsulates the heuristic function
           ab_enable determines whether we use alpha-beta pruning in the search
           player_first determines if the user plays first
        output is the final game state
        '''
        self.reset_stats()
        state = game.get_initial_state()
        color = 1
        game.print_state(state)

        if not player_first:
            if not game.terminal(state):
                print("COMPUTER PLAYER TURN: ")
                state = self.computer_move(game, heur_fn, state, color, ab_enable)
                game.print_state(state)
                color *= -1

        while 1:
            if game.terminal(state):
                break
            print("USER PLAYER TURN: ")
            state = self.player_move(game, state, color)
            game.print_state(state)
            color *= -1

            if game.terminal(state):
                break
            print("COMPUTER PLAYER TURN: ")
            state = self.computer_move(game, heur_fn, state, color, ab_enable)
            game.print_state(state)
            color *= -1

        self.total_search_time = time.time() - self.total_search_time
        if self.trace:
            self.print_endgame(game, state)
        return state

    def computer_vs_computer(self, game, heur_fn1, heur_fn2, ab_enable=False):
        '''2 computer players play against each other.
        input:
            game is the Game object
            heur_fn1 is a Heuristic object that encapsulates the first player's heuristic function
            heur_fn2 is a Heuristic object that encapsulates the second player's heuristic function
            ab_enable determines whether we use alpha-beta pruning in the search
        output is the final game state
        '''
        self.reset_stats()
        state = game.get_initial_state()
        color = 1
        if self.trace:
            game.print_state(state)

        while 1:
            if game.terminal(state):
                break
            state = self.computer_move(game, heur_fn1, state, color, ab_enable)
            if self.trace:
                print("COMPUTER PLAYER 1 TURN: ")
                game.print_state(state)
            color *= -1

            if game.terminal(state):
                break
            state = self.computer_move(game, heur_fn2, state, color, ab_enable)
            if self.trace:
                print("COMPUTER PLAYER 2 TURN: ")
                game.print_state(state)
            color *= -1

        self.total_search_time = time.time() - self.total_search_time
        if self.trace:
            self.print_endgame(game, state)
        return state

    def print_endgame(self, game, state):
        '''Prints the winner of the game.
        input:
            game is the Game object
            state is the final endgame state
        '''
        winner = game.winner(state)
        if winner == GAME_P1_WIN:
            print("P1 WINS")
        elif winner == GAME_P2_WIN:
            print("P2 WINS")
        else:
            print("TIE")

        print("TIME PLAYED = {}, STATES EXPANDED = {}".format(self.total_search_time,search.nm_st_exp))
