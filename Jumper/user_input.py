# User Input: (Ethan)
#  Has:
#     - list of unguessed letters (built in function --> ASCII lower)
#     - list of guessed letters

#  Does:
#     - Get valid input from the user (single character) <-- checks within ASCII lowercase list
#      - To lower any capital input
#      - not a number or symbol
#      - Check for repeat letters

import string

class UserInput:
    
    def __init__(self):
        self._unguessed = list(string.ascii_lowercase)
        self._guessed = []

    
    def get_input(self):
        guess = input("Guess a letter [a-z]: ")
        guess = guess.lower()
        guess_length = len(guess)

            # makes sure there is only 1 alpha character
        if guess_length >= 2 or guess.isalpha() == False:
            print("Limit guess to a singular alpha character")

            #checks and rejects repeat letters
        else:
            for x in self._guessed:
                if x == guess:
                    print('This letter has already been guessed. Guess a letter that has not been guessed.')
                    break

                # removes guess from unguessed list and adds guess to guessed list    
            for x in self._unguessed:
                if x == guess:
                    index = x.index()
                    self._unguessed.pop(index)
            self._guessed.append(guess)

            return guess