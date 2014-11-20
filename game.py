
class Heuristic:
    '''Heuristic object encapsulates a heuristic function, including lower and upper bounds.'''

    def heuristic(self, game, state):
        '''The heuristic function, strictly bounded by a lower and upper bound.
        input:
           game is the Game object
           state is the state for which we want a heuristic estimate
        output is a value between self.get_lower_bound() and self.get_upper_bound(), exclusive
        Must override.
        '''
        pass

    def get_lower_bound(self):
        '''A strict lower bound on the heuristic function.
        Must override.
        '''
        pass

    def get_upper_bound(self):
        '''A strict upper bound on the heuristic function.
        Must override.
        '''
        pass

class ZeroHeuristic(Heuristic):
    ''' A simple, uninformed heuristic valid for any game.'''

    def heuristic(self, game, state):
        '''Return upper_bound-1 if P1 wins, lower_bound+1 if P2 wins, 0 otherwise.'''
        winner = game.winner(state)
        if (winner == GAME_NONTERMINAL) or (winner == GAME_TIE):
            return 0
        return 1000 if (winner == GAME_P1_WIN) else -1000

    def get_lower_bound(self):
        return -1001

    def get_upper_bound(self):
        return 1001

# Return values for game.winner
GAME_P1_WIN = 1
GAME_P2_WIN = -1
GAME_TIE = 0
GAME_NONTERMINAL = 3

class Game:

    '''Encapsulates a game. Properly deriving each of the following functions will enable this game
       to be played by the GameEngine class.'''

    def get_initial_state(self):
        '''Returns the initial game state.
        Must override.'''
        pass

    def winner(self, state):
        '''Returns
           GAME_P1_WIN if player 1 (color 1) wins in state
           GAME_P2_WIN if player 2 (color -1) wins in state
           GAME_TIE if terminal and neither player wins in state
           GAME_NONTERMINAL if state is not a terminal state
        Must override.'''
        pass

    def terminal(self, state):
        '''Returns True if state is terminal, False otherwise.
        Must override.'''
        pass

    def moves(self, player, state):
        '''Returns a list of valid moves that player can execute in state.
        input:
            player is either 1 (player 1) or -1 (player 2)
            state is the state we want valid moves for
        output is a list of valid moves
        Must override.'''
        pass

    def next_state(self, player, state, move):
        '''Returns the resulting state if action move is executed in state by player
        input:
            player is either 1 (player 1) or -1 (player 2) that executes the move
            state is the state we start from
            move is the move we execute
        output is the resulting state
        Must override.'''
        pass

    def parse_player_move(self, move_str):
        '''Returns a valid move if move_str is a valid move string, otherwise it returns a non-valid move.
        input:
           move_str is the string we wish to convert to a valid move
        output is a valid move if move_str is correct, otherwise it is an 
           invalid move (such that calling self.valid_move on it will return False)
        Will be provided.'''
        pass

    def valid_move(self, state, proposed):
        '''Returns True if action proposed is valid (executable) in state, False otherwise
        input:
           state is the state the action will be executed in
           proposed is the action that is being tested for validity
        output is True if proposed is valid, False otherwise
        Must override.'''
        pass

    def print_state(self, state):
        '''Prints the input state. 
        Will be provided'''
        pass
