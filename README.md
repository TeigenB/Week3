# Week3
Hilo is a game in which the player guesses if the next card drawn by the dealer will be higher or lower than the previous one. Points are won or lost based on whether or not the player guessed correctly.

The player starts the game with 300 points.
Individual cards are represented as a number from 1 to 13.
The current card is displayed.
The player guesses if the next one will be higher or lower.
The the next card is displayed.
The player earns 100 points if they guessed correctly.
The player loses 75 points if they guessed incorrectly.
If a player reaches 0 points the game is over.
If a player has more than 0 points they decide if they want to keep playing.
If a player decides not to play again the game is over.
Designing Classes:
1. look for nouns to identify objects in the game.
2. define responsibility, behaviors and state for each object. look for related verbs
3. identify the relationships between objects. look at ui to help
4. translate your object designs to class designs. class and method names, parameters, data types
5. document objects and classes so everyone can refer to them.

Class: Game
Method: Initialize Game(self)

Method: Start Game(self)
-I think this is here so that you can run multiple rounds of the game without having to completely exit out and restart the program
-Display the starting score of 300 points
-Return True/False (for if wanting to CONTINUE playing)

Method: User Input(self)
-Show the current card
-Ask the user if the next card is higher or lower
-return CHOICE (int:1=high 2=low)

Method: Point Update(self)
-Add 100 points to the existing score or subtract 75 points from the existing score
-Return POINTS (int)

Method: Output(self)
-If current point value is > 0 run a message asking if player wants to keep going
-If player answers no, run game end method
-Return CONTINUE (Which will infuence true/false method for game end)

Method: Game end(self)
-If current point value is <= 0 run an end game message and run the initialize method on a new game
-Also if CONTINUE is false then end game


Class: Dealer(self)
Method: Generate deck (self)
-Initializes the class and starts a new instance
-Return DECK (array)

Method: Generate Card(self)
-Will generate a card with a random number between 1 and 13
-Return CARD (int)

**Good design. Never understood classes the way this is designed.