from game import *



#The provided function here is a copy of the ZeroHeuristic in game.py
#It is your job to alter this to make an improved heuristic
class MancalaHeuristic(Heuristic):


    #Alter this function
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





class Mancala(Game):


    '''
    pits indicates the number of pits in each row
    stonesPerPit indicates the number of initial stones in each pit
    To be implemented'''
    def __init__(self, pits, stonesPerPit):


    '''Returns the initial game state.
    To be implemented'''
    def get_initial_state(self):
        
    '''Returns:
    GAME_P1_WIN if player 1 (color 1) wins in state
    GAME_P2_WIN if player 2 (color -1) wins in state
    GAME_TIE if terminal and neither player wins in state
    GAME_NONTERMINAL if state is not a terminal state
    To be implemented'''
    def winner(self, state):
        
    '''Returns True if state is terminal, False otherwise.
    To be implemented.'''
    def terminal(self, state):
        
        
    '''Returns a list of valid moves that player can execute in state.
    input:
        player is either 1 (player 1) or -1 (player 2)
        state is the state we want valid moves for
    Returns a list of valid moves

    !!NOTE: moves should be a single number as described in the problem 
    description

    To be implemented.'''
    def moves(self, player, state):


    '''Returns the resulting state if action move is executed in state by player
        input:
            player is either 1 (player 1) or -1 (player 2) that executes the move
            state is the state we start from
            move is the move we execute
        Returns the resulting state
    To be implemented.'''
    def next_state(self, player, state, move):


    '''Returns a valid move if move_str is a valid move string, otherwise it returns a non-valid move.
        input:
           move_str is the string we wish to convert to a valid move
        Returns a valid move if move_str is correct, otherwise it is an 
           invalid move (return -1)
    To be implemented'''
    def parse_player_move(self, move_str):

        
    '''Returns True if action proposed is valid (executable) in state, False otherwise
        input:
           state is the state the action will be executed in
           proposed is the action that is being tested for validity
        Returns True if proposed is valid, False otherwise
    To be implemented'''
    def valid_move(self, state, proposed):

    
    '''Prints the input state. 
    Must be implemented, but will not be graded
    Useful for debugging and information purposes'''
    def print_state(self, state):



#debugging code
if __name__ == '__main__':

    from game_engine import *

    game = Mancala(6,4)

    #The 3 here indicates maximum search depth, feel free to alter this in your tests
    engine = GameEngine(3, 1)

    engine.computer_vs_computer(game, ZeroHeuristic(), MancalaHeuristic(), True)

    #engine.play allows a human to play against the specified heuristic
    #uncomment to try this tests
    #engine.play(game, ZeroHeuristic(), True, False)
