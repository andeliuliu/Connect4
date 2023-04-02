#
# ps9pr1.py (Problem Set 9, Problem 1)
#
# A Connect Four Board class
#
# Computer Science 111
#

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    ### add your constructor here ###
    def __init__(self, height, width):
        """a constructor for board objects"""
        self.height = height
        self.width = width
        self.slots = [[' '] * width for r in range(height)]
        
    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''        

        for row in range(self.height):
            s += '|'  
            for col in range(self.width):
                s += self.slots[row][col] + '|'
            s += '\n'
        s += '-' * (2 * self.width) + '-' + '\n'
        for x in range(self.width):
            s += ' ' + str(x)
                    
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        ### put the rest of the method here ###
        row = 0 
        while self.slots[row][col] == ' ':
            row += 1
            if row == self.height:
                break
        self.slots[row-1][col] = checker 
        
    
    ### add your reset method here ###
    
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def reset(self):
        """Clears the Board on which it is called by setting all slots to contain a " " """
        for row in range(self.height):
            for col in range(self.width):
                    self.slots[row][col] = ' '
    
    def can_add_to(self, col):
        """checks to see if there is an open slot in the given column"""
        if col < 0 or col >= self.width:
            return False
        elif self.slots[0][col] != ' ':
            return False
        else:
            return True
    
    def is_full(self):
        """checks to see if the board is full"""
        for col in range(self.width):
           if self.can_add_to(col):
               return False
           
        return True
       
    
    def remove_checker(self, col):
        """removes the checker in the given slot""" 
        for x in range(self.height):
            if self.slots[x][col] != ' ':
                break 
        self.slots[x][col] = ' '
    
    def is_win_for(self, checker):
        """ determines whether the specified checker has a win
        """
        assert(checker == 'X' or checker == 'O')
        if self.is_horizontal_win(checker):
            return True
        elif self.is_vertical_win(checker):
            return True 
        elif self.is_down_diagonal_win(checker):
            return True
        elif self.is_up_diagonal_win(checker):
            return True
        else:
            return False
        
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
            # Check if the next four columns in this row
            # contain the specified checker.
                if self.slots[row][col] == checker and \
                    self.slots[row][col + 1] == checker and \
                        self.slots[row][col + 2] == checker and \
                            self.slots[row][col + 3] == checker:
                   return True

    # if we make it here, there were no horizontal wins
        return False
    
    def is_vertical_win(self, checker):
        """returns True if the checker has 4 in a row vertically"""
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                    self.slots[row + 1][col] == checker and \
                        self.slots[row + 2][col] == checker and \
                            self.slots[row + 3][col] == checker:
                    return True
    
    def is_up_diagonal_win(self, checker):
        """returns True if the checker has 4 in a row diagonally down"""
        for row in range(3, self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                    self.slots[row - 1][col + 1] == checker and \
                        self.slots[row - 2][col + 2] == checker and \
                            self.slots[row - 3][col + 3] == checker:
                    return True         
                
    def is_down_diagonal_win(self, checker):
        """returns True if the checker has 4 in a row diagonally up"""
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                    self.slots[row + 1][col + 1] == checker and \
                        self.slots[row + 2][col + 2] == checker and \
                            self.slots[row + 3][col + 3] == checker:
                    return True 
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        