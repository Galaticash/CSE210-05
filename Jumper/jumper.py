class Jumper():
    def __init__(self):
        # Each portion of the parachute with escaped characters
        self._parachute = [""," ___", "/___\\", "\   /", " \ /", "  0", " /|\\", " / \\", "", "^^^^^^^"]
        self._man = ["", "  x", " /|\\", " / \\", "", "^^^^^^^"]
        self._health = 4
        self._alive = True

    def print_jumper(self):
        for line in self._parachute:
            print(line)

    def print_failure(self):
        for line in self._man:
            print(line)

    def remove_line(self):
        self._parachute.pop(1)
        self._health -= 1
        self._alive = self._health > 0 

    def get_alive(self):
        return self._alive