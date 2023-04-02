    #
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below.
class Player: 
    def __init__(self, checker):
        "constructs a new Player object"
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        """returns a string representing a Player object"""
        if self.checker == 'O':
            return "Player O"
        elif self.checker == 'X':
            return "Player X"
    
    def opponent_checker(self):
        """returns a string representng an opponent object"""
        if self.checker == 'O':
            return 'X'
        elif self.checker == 'X':
            return 'O'

    def next_move(self, b):
        """returns the column where the player wants to make the next move"""
        self.num_moves += 1
      
        while self.num_moves > 0:
            col = int(input("Enter a column: "))
            if b.can_add_to(col) == True:
                return col 
            else:
                print("Try again!")

        
        