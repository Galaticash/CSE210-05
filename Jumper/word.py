class Word:
    def __init__(self):
        #sets the word and guessed word to an empty string, calls underscore to fill the guessed word with blanks
        self._word = ""
        self._guessed_word = ""
        self._guessed_letters = []
        self._all_guessed = False
        self.underscore()
    
    #using a property decorator to set the word and set it to the empty word property
    def set_word(self, word):
        self._word = word

    def underscore(self):
        #sets the guessed word with underscores for unguessed letters
        for i in range(len(self._word)):
            self._guessed_word += "_"

    #using a property decorator to set a guessed letter, keep track of it in an array, check for matches, and replace the underscore with the letter
    def set_guess_letter(self, _letter):
        self._guessed_letters.append(_letter)
        if _letter in self._word:
            for i in self._word:
                if i == self._guessed_letter:
                    #build new guessed word with the letter
                    _index = self._guessed_word.index(self._guessed_letter)
                    self._guessed_word = self._guessed_word[:_index] + self._guessed_letter + self._guessed_word[_index+1:]
            return True
        else:
            return False            
        
    def guess_checker(self):
        if self._guessed_word == self._word:
            self._all_guessed = True