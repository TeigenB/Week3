
class game:

#Methods 1

    def __init__(self):
        """Initiates a new game with is_playing and point_value as attributes"""
        self.is_playing = True
        self.point_value = 300
        
#Methods 2-4
    """These functions will go through a round of the game. """"
    def start_round(self):
        pass
    def input(self):
        pass
    def update_points(self):
        pass

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




