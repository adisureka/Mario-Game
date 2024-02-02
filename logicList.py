import random
class LogicList():

    master_list: list
    archive_list: list
    size: int

    def __init__(self, size = 4):
        '''
        Method:    This is backend of the game, in this object, create a list represent
                   the game, the list to __str__ like the following
                    <backend list>
                   [
                      1   2   3   4
                      5   6   7   8
                      9  10  11  12
                     13  14  15  16
                                     ]
                    number 16 represent the blank tile 
                    win is the shuffle list __eq__to the initial list
        Parameter: self, size
        Return   : None
        '''
        self.size = size
        self.master_list = [i + 1 for i in range(self.size * self.size)]
        self.archive_list = self.master_list.copy()

    def __str__(self):
        '''
        Method:    this method print out this object
        Parameter: self
        Return   : None
        '''
        return self.list_to_string()

    def __eq__(self, other):
        '''
        Method:    this method check if two objects are the same
        Parameter: self
        Return   : boolean
        '''
        return self.master_list == other.master_list

    def get_list(self):
        '''
        Method:    this method return the list
        Parameter: self
        Return   : list
        '''
        return self.master_list

    def back_to_original(self):
        self.master_list = self.archive_list.copy()

    def shuffle(self):
        random.shuffle(self.master_list)

    def list_to_string(self)->str:
        """
        Function : read the master_list and pseudo separate them into 4 list
                   to print out
        Parameter: self
        Return   : string
        """
        
        display_str = "[\n"
        for i in range(self.size):
            for j in range(self.size):
                display_str += f" {self.master_list[i * self.size + j]:3}"
            if i < self.size - 1:
                display_str += "\n"
            else:
                display_str += f"\n{']':>19}"
        return display_str
    
    def swap_backend(self, from_num)->bool:
    	if self.is_valid(from_num):
    		to_index = self.master_list.index(16)
    		from_index = self.master_list.index(from_num)
    		self.master_list[to_index] = from_num
    		self.master_list[from_index] = 16
    		return True
    	else:
    		print("this is not a valid move")
    		return False

    def is_valid(self, from_num)->bool:
        """
        Function : this function check whether the 'zero' is on the left, right 
                   up and down of the given number
        Parameter: number
        Return   : bool
        """

        from_index = self.master_list.index(from_num)

        if from_index - 1 >= 0:            
            if self.master_list[from_index - 1] == 16:
                # special case if number are at the pseudo table first column
                # and the 0 is at the pseudo table last column, it will miscalculate
                # as a valid because 1d list, we should avoid running this if statement
                if from_index % self.size == 0:
                    return False    
                return True
        
        # on the right
        if from_index + 1 < self.size * self.size:
            if self.master_list[from_index + 1] == 16:
                if from_index % self.size == self.size - 1:
                    return False 
                return True    
        
        # on the top
        if from_index - self.size >= 0:
            if self.master_list[from_index -self.size] == 16:
                return True
        # on the bottom
        if from_index + self.size < self.size * self.size:
            if self.master_list[from_index + self.size] == 16:
                return True
        return False 
        
