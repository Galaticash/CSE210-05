#Creates a list of 20 words long of five letter words
#Randomly chooses one five letter word


import random 

class WordGetter(): 
    def __init__(self):
        self._wordlist = ["water", "house", "think", "years", "small", "large", "study", "night", "paper", "table", 
        "order", "black", "horse", "green", "river", "field", "leave", "winds", "zesty", "maybe"]

        return(random.choice(self._wordlist))


