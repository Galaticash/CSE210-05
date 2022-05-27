class Word:
    def __init__(self):
        #sets the word and guessed word to an empty string, calls underscore to fill the guessed word with blanks
        self._word = ""
        self._guessed_word = ""
        self._guessed_letters = []
        self._all_guessed = False

    # Generates the guessed_word string
    def underscore(self):
        #sets the guessed word with underscores for unguessed letters
        for i in range(len(self._word)):
            self._guessed_word += "_"

    # Sets the word, splits string into list of characters
    def set_word(self, word):
        self._word = word
        self.underscore()

    # If the word has been completely guessed
    def get_complete(self):        
        return self._all_guessed

    # Returns the word with "_" in place of unguessed letters
    def get_current_word(self):
        return self._guessed_word

    # Given a guessed letter from the user (already sanatized), will see if it 
    # is in the word and then update the "_" version
    def guess_letter(self, letter):
        self._guessed_letters.append(letter)
        # If the guessed letter is in the word
        if letter in self._word:
            for i in range(len(self._word)):
                if self._word[i] == letter:
                    #logic is sketch, thinking this one over, slicing in python is weird.
                    # Update the "_" version
                    self._guessed_word = self._guessed_word[:i] + letter + self._guessed_word[i+1:]
            if self._guessed_word == self._word:
                self._all_guessed = True
            return True       
        else:
            # The guessed letter is NOT in the word
            return False