# The-Snake-Game
## Goals:
Play the all-time classic snake-game (sometimes called snake xenia), where the objective is to direct the 'snake' to eat bits of 'food' that randomly appears on the screen, making its length increase. 

## Gameplay and Directions:
+ Use the 'Up', 'Down', 'Left' and 'Right' arrow keys to control the snake's movements
+ Optional: If you are familiar with the Turtle module, you may toggle to the corresponding part of the code in main.py and change the control keys
+ Yellow coloured dots representing food appears on random places on the screen on at a time
+ Direct the snake towards the 'food'. If the snake's 'head' touches the 'food', the 'food' is ingested and the length of the snake's body increases
+ Upon the snake head's collision with the 'food', the 'food' disappears, and reappears at another place on the screen
+ Each time your snake 'eats' a 'food', the score increases by one. Your current score can be seen on the top of the playing screen
+ The game continues and the snake's length keep increasing until the snake head:
  1. Touches any of the edges of the screen OR
  2. The head bumps into its own tail
+ In case of any of the above two cases happening, the game ends and the score is displayed on the screen

## Additional Points
+ The snake.py, food.py and scoreboard.py all contain classes that are referenced to in the main.py file. Therefore, it is preferred that all four files be contained within the same folder
+ To use the code, you must copy and paste it into your IDE or code editor and run it there
+ All the graphics have been created using the Turtle module
+ The turtle module documentation can be accessed here: https://docs.python.org/3/library/turtle.html 
  
