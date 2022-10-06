class game:

#Methods 1

    def __init__(self):
        """Initiates a new game with is_playing and point_value as attributes"""
        self.is_playing = True
        self.point_value = 300
        self.current_card = ""
        self.higher = ""
        self.lower = ""
        self.choice = 0
        self.score = 0
        self.total_score = 0
        
#Methods 2-4
    """These functions will go through a round of the game. """
    def start_round(self):

        pass

#Method 3
    def input(self):
        """Ask the user if the next card is higher or lower. (Josiah)"""
        self.current_card = ""
        self.next_card = input("Is next next higher or lower?")
        self.is_playing = (self.next_card == "y")
        if self.is_playing == self.higher:
            self.choice = 1
        if self.is_playing == self.lower:
            self.choice = 2
        return self.choice

    #Method 4
    def update_points(self):
        """Updates the player's score.(Josiah)"""
        if not self.is_playing:
            return

        for i in range(len(self.value)):
            card = self.value[i]
            card.generate()
            self.score += card.points 
        self.total_score += self.score

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