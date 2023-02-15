import random

class BoggleBoard:
    starting_row = ["_","_","_","_"]
    def __init__(self)-> None:
        self.rows = [[*self.starting_row],[*self.starting_row],[*self.starting_row],[*self.starting_row]]
    
    # function prints each elem in each row of self so that the output looks like a board
    # joins each elem in a row and prints      
    def show_board(self):
        for row in self.rows:
            print(self.printable_row(row))
    
    # used by show board to join the letters in each row as a cohesive board
    def printable_row(self, row):
        return ''.join(row)
    
    # this fn uses list_of_dice to implement 16 die with each side of the die representing a letter in the string
    # then loops until list of die is empty meaning all dice have been chosen
    # also loops through each elem in every row of self.rows and replaces the "_" with a random letter from a random die
    # (random index and radom elem from list_of_dice)
    def shake(self):
        list_of_dice = ['AAEEGN', 'ELRTTY', 'AOOTTW', 'ABBJOO', 'EHRTVW', 'CIMOTU', 'DISTTY', 'EIOSST', 'DELRVY','ACHOPS', 'HIMNQU', 'EEINSU', 'EEGHNW', 'AFFKPS', 'HLNNRZ', 'DEILRX']
        while len(list_of_dice) > 0:
            for row in self.rows:
                for index, elem in enumerate(row):
                    dice_roll = random.randint(0,5)
                    elem = random.choice(list_of_dice)
                    list_of_dice.remove(elem)
                    row[index] = elem[dice_roll] + '  '
                    
                    if row[index] == 'Q  ':
                        row[index] = 'Qu'
                
        return self.show_board()
        
    
dice = set()
d = {'dice1' : [1,2,3,4,5], 'dice2' : [6,7,8,9,0]}

dice.add(random.choice(list(d.keys())))

new_board = BoggleBoard()

new_board.shake()