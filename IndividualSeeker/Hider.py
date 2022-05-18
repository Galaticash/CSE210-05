import random
# Changable range for hiding
SEEKER_MAX = 1000

class Hider:
    def __init__(self):
        self._max_hiding = SEEKER_MAX
        self._position = 0

    # Get the max range of the hider's location
    def get_max_hiding(self):
        return self._max_hiding

    # Find where the Hider is currently hiding
    def get_position(self):
        return self._position

    # The hider will find a random location between 1 and max to hide
    def hide(self):
        self._position = random.randint(1, SEEKER_MAX)
