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

            # .index() only works on a list, with the value given as a parameter
            # Example: list.index(value) --> returns the index of value in the list
            # for x in self._unguessed:
            #     if x == guess:
            #         index = x.index()
            #         self._unguessed.pop(index)

            # Here's one way I found to pop the unguessed list, it also
            #   doubles as a check to see if a letter is no longer in the list, 
            #   since using .index() with a value that is not in the list
            #   will throw an error.
            
            # This try/except clause will try what is in the 'try' section
            #   and if an error is thrown, it will do what is in the 'except' section
            try:
                index = self._unguessed.index(guess)
                self._unguessed.pop(index)
            except:
                print("Already guessed *") # Remove previous 'for' loop and then put message here?

            self._guessed.append(guess)

            return guess


# This line means: If running file as the main program,
# Convienient for debugging single files, remove later
if __name__ == "__main__":
    DEBUGGING = True
    # Create an instance of UserInput to use
    user_input_test = UserInput()

    # This is an infinite loop, exit/kill terminal to quit
    while DEBUGGING:
        # Missing:
        #       - when there is a repeat letter, ask for a new one (currently returns the repeated letter)
        #       - when there is an invalid letter, ask for a new one (currently returns None)
        # Basically, have a while loop inside the function and escape it by returning a valid guess
        user_guess = user_input_test.get_input()

        # See what the method returned
        print(f"The user guessed the letter '{user_guess}'")