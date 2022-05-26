# Import additional classes after they are created
# from word_getter import WordGetter
# import Word
# import Jumper
from user_input import UserInput

class Director:
    def __init__(self):
        self._game_over = False
        # self._word_generator = WordGetter()
        # game_word = Word()
        # jumper = Jumper()
        self._user_input = UserInput()

    def play_game(self):
        # Randomly pick a word from the list of Words that the Word Getter/Generator object has
        print("[Word Getter] Missing method: Get a random word (string)")
        #self._word = self._word_generator.get_word()
        
        self._word = "three"
        # [Word] Method: get/set word
        # game_word.set_word(self._word)

        # Play the game until it is over (run out of parachute or correctly guesses)
        while not self._game_over:
            # Print the word (with underscores for unguessed letters)
            print("[Word] Missing method: Print underscores and guessed letters")
            
            # Print the Jumper ASCII art, visual shows how many guesses are left before losing
            print("[Jumper] Missing method: Print Jumper")
           
            # Ask the user to guess a letter, verifying that they input a single letter (not already guessed)
            user_guess = self._user_input.get_input()

            # Check if the user's letter guess is in the word
            print("[Word] Missing method: Check if letter is in the word (True/False)")
            correct_guess = True

            # If the letter is not in the word
            if not correct_guess:
                # Update the Jumper to remove a line of the parachute
                print("[Jumper] Missing method: Remove a line from the parachute")
                
                # Find out if the Jumper still has some parachute left, or if the user is out of guesses
                print("[Jumper] Missing method: Get Jumper alive state (True/False)")
                jumper_alive = False

                # If the user is out of guesses
                if not jumper_alive:

                    # The game is over, user loses
                    self._game_over = True
                    print(f"The word was \"{self._word}\"")
            else:
                # Check if the user has completed the word with their guess
                print("[Word] Missing method: Check if word is complete (True/False)")
                word_complete = True
                

                # If all letters in the word have been guessed
                if word_complete:

                    # The game is over, user wins
                    self._game_over = True
                    print("You guessed the word!")

        # The game is over, could print a "You won!" or "You lost" message
        print("Game over")