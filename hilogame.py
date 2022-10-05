
class game:

#Methods 1

    def _init_(self):
        self.is_playing = True
        self.point_value = 400
#Methods 2-4
#
#Method 5
    def do_output(self):
        if not self.is_playing:
            return
        elif self.point_value > 0:
            print("Would you like to keep going?")
            self.is_playing = input("y/n: ")
            if self.is_playing == "n":
                pass
                #run game end method, which will display score and run initialize game
        elif self.point_value < 0:
            #display score
            #Run game init
            pass

#Method 6
    def end_game(self):
        pass


