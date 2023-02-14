import random

class GuessingGame:
    def __init__(self, answer, solved = False) -> None:
        self.answer = answer
        self.solved = solved
        
game = GuessingGame(random.randint(1,100))

while not game.solved:
    guess = input("Enter your guess: ")
    if guess == game.answer:
        game.solved = True
        print('Correct!')
    else:
        print('Guess again')
    