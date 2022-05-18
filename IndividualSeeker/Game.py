from Hider import Hider

# Director class
class Game:
    def __init__(self):
        self._hider = Hider()
        self._game_over = False
        self._user_guess = 0
        self._prev_closeness = 0

    # Method, part of the class/object 
    def play(self):
        
        # The hider will choose a random location to hide
        self._hider.hide()

        while not self._game_over:
            # Ask the user to guess a location (validating that the integer is within the hiding range)
            self._user_guess = valid_int_input(f"Enter a location [1-{self._hider.get_max_hiding()}]: ", 1, self._hider.get_max_hiding())

            # Determine how close the guess is
            closeness = abs(self._hider.get_position() - self._user_guess)
            # print(f"{self.hider._position}") <-- should NOT be used, private variable

            # Tell the user if they are closer or further away
            # Actually guessed it
            if closeness == 0:
                print("You found me!")
                self._game_over = True
            # If the guess is further away
            elif closeness > self._prev_closeness:
                print("You are further away!")
            # If the guess is closer
            elif closeness < self._prev_closeness:
                print("You are closer!")
            else:
                print("Same distance away, count as colder?")

            # Prepare for next turn, current becomes previous.
            self._prev_closeness = closeness

# Function, I left it out of the Game class
def valid_int_input(message, min_int, max_int):
    """ Get a valid integer input within a given range.
        Repeats message until user enters a valid integer.
        Returns a user-inputed integer.
    """
    # Initialize values
    user_input = 0
    valid_input = False

    # While the user has not entered a valid input,
    while not valid_input:
        try:
            # Ask the user for an integer input.
            user_input = int(input(f"{message} "))
            # Exceptions will be thrown if not an integer.
            # Check if the integer is too low or too high.
            if user_input < min_int:
                print(f"Please enter a value greater than {min_int}")
            elif user_input > max_int:
                print(f"Please enter a value less than {max_int}")
            else:
                # Integer is within the range, valid input.
                valid_input = True
        except ValueError:
            print("Please enter an integer")
        except:
            print("An error occurred")
    
    # Return the user's integer input.
    return user_input
