from card import Dealer
class game:
#this is a test
#Methods 1

    def __init__(self):
        """Initiates a new game with is_playing and point_value as attributes"""
        self.is_playing = True
        self.point_value = 300
        self.current_card = ""
        self.higher = ""
        self.lower = ""
        self.choice = 0
        self.next_card = 0
        self.user_input = 0
        self.card = ""
        
#Methods 2
    """These functions will go through a round of the game. """
    def start_round(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (game): an instance of game.
        """
        while self.is_playing:
            self.input()
            self.update_points()
            self.output()

#Method 3
    def input(self):
        """Generate and print the current card."""
        self.current_card = self.card.generate()
        print(f"The current card is {self.current_card}")

        self.next_card = self.card.generate()
        print("Is next next card higher or lower?")
        self.user_input = input("[h/l]")
        if self.user_input == "h":
            self.choice = 1
        if self.is_playing == "l":
            self.choice = 2
        return self.choice

    #Method 4
    def update_points(self):
        """Updates the player's score.git"""
        if not self.is_playing:
            return

        if self.choice == 1:
            self.point_value += 100
        if self.choice == 2:
            self.point_value -= 75
        else:
            self.point_value = 0

#Method 5
    def output(self):
        """Displays the score and will evaluate if the user is able to or wants to keep playing.
        Arguments: 
        """
        if not self.is_playing:
            return
        elif self.point_value > 0:
            print(f"Your score is {self.point_value}. Would you like to keep going?")
            self.is_playing = input("y/n: ")
            if self.is_playing == "n":
                self.end_game()
            elif self.is_playing == "y":
                self.start_round()
        elif self.point_value < 0:
            print("You have no more points to play")
            self.end_game()

#Method 6
    def end_game(self):
        while not self.is_playing:
            print(f"Your score was {self.point_value}")
            self.point_value == 300
            self.is_playing = True
