#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    
    def __init__ (self, checker, tiebreak, lookahead):
        """constructs a new AIPlayer object"""
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0) 
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    def __repr__(self):
        """returns the string of the AIPlayer method"""
        method = ''
        method += 'Player ' + str(self.checker) + " (" + str(self.tiebreak) + ", " + str(self.lookahead) + ")"
    
        return method
    
    def max_score_column(self, scores):
        """takes the input of scores and returns the index of the list based on whether the self.tiebreak is left, right or random"""
        maxList = []
        maxScore = max(scores)
        for x in range(len(scores)): 
            if scores[x] == maxScore:
                maxList += [x]
        if self.tiebreak == 'LEFT':
            return maxList[0]
        if self.tiebreak == 'RIGHT':
            return maxList[-1]
        if self.tiebreak == 'RANDOM':
            return random.choice(maxList)

    def scores_for(self, b):
        """returns a list of scores for each of the columns in the b object"""
        scores = [50] * b.width
        for col in range(b.width):
            if b.can_add_to(col) == False: 
                scores[col] = -1
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead-1)
                opp_scores = opponent.scores_for(b)
                if max(opp_scores) == 100:
                    scores[col] = 0
                if max(opp_scores) == 50:
                    scores[col] = 50
                if max(opp_scores) == 0:
                    scores[col] = 100
                b.remove_checker(col)
        return scores 
    
    def next_move(self, b):
        """returns the best move for the AIPlayer""" 
        self.num_moves += 1
        
        scores = self.scores_for(b)
        col = self.max_score_column(scores)
  
        return col 
            