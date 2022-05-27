# Import additional classes after they are created
from word_getter import WordGetter
from word import Word
from jumper import Jumper
from user_input import UserInput

class Director:
    def __init__(self):
        self._game_over = False
        self._word_generator = WordGetter()
        self._game_word = Word()
        self._jumper = Jumper()
        self._user_input = UserInput()

    def play_jumper(self):
        """
            Plays the Jumper game, where the user is to guess a word by
             guessing it letter by letter. They can only get so many
             guesses wrong before their Jumper looses their parachute.
        """
        # Randomly picks a word from the list of Words 
        #   that the Word Getter/Generator object has.
        self._word = self._word_generator.get_word()

        # Give Word the game's word
        self._game_word.set_word(self._word)

        # Play the game until it is over.
        #   (Runs out of parachute or correctly guesses)
        while not self._game_over:
            self.print_screen()
            
            # Ask the user to guess a letter, verifying that they input 
            #   a single alphabet letter. (Not already guessed)
            user_guess = self._user_input.get_input()

            # Check if the user's letter guess is in the word.
            correct_guess = self._game_word.guess_letter(user_guess)

            # If the letter is not in the word,
            if not correct_guess:
                # Update the Jumper to remove a line of the parachute.
                #print("[Jumper] Missing method: Remove a line from the parachute")
                self._jumper.remove_line()

                # Find out if the Jumper still has some parachute left,
                #   or if the user is out of guesses.
                #print("[Jumper] Missing method: Get Jumper alive state (True/False)")
                jumper_alive = self._jumper.get_alive() # DEBUGGING: Will automatically end game

                # If the user is out of guesses,
                if not jumper_alive:

                    # The game is over, user loses.
                    self._game_over = True
                    self.print_screen("lose")
                    print(f"The word was \"{self._word}\"")
            else:
                # Check if the user has completed the word with their guess.
                word_complete = self._game_word.get_complete()

                # If all letters in the word have been guessed,
                if word_complete:

                    # The game is over, user wins.
                    self._game_over = True
                    self.print_screen("win")
                    print("You guessed the word!")

    def print_screen(self, state = "game"):
        """
            Prints the word and the jumper states. Special states have 
              been created for if the player wins or loses.
        """
        # Prints the word with underscores for unguessed letters.
        print(self._game_word.get_current_word())

        # Print the Jumper ASCII art, visually shows how many
        #   guesses are left before losing.
        if state == "game":
            self._jumper.print_jumper()
        elif state == "win":
            self._jumper.print_success()
        elif state == "lose":
                self._jumper.print_failure()

if __name__ == "__main__":
    director_test = Director()
    director_test.play_jumper()