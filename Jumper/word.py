from msilib.schema import Class


class Word:
    def __init__(self):
        #sets the word and guessed word to an empty string, calls underscore to fill the guessed word with blanks
        self._word = ""
        self._guessed_word = ""
        self._guessed_letters = []
        self._all_guessed = False
        self.underscore()
    
    #using a property decorator to get the word and set it to the empty word property
    @property
    def word(self):
        return self._word

    def underscore(self):
        #sets the guessed word with underscores for unguessed letters
        for i in range(len(self._word)):
            self._guessed_word += "_"

    #using a property decorator to get a guessed letter, keep track of it in an array, check for matches, and replace the underscore with the letter
    @property
    def guess_letter(self):
        self._guessed_letters.append(self._guessed_letter)
        if self._guessed_letter in self._word:
            for i in (self._word):
                if self._word[i] == self._guessed_letter:
                    #logic is sketch, thinking this one over, slicing in python is weird.
                    self._guessed_word = self._guessed_word[:i] + self._guessed_letter + self._guessed_word[i+1:]
        if self._guessed_word == self._word:
            self._all_guessed = True