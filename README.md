<h1 style="font-size: 40px;">Snake Game Documentation</h1>
  
This is a simple snake game implemented in Python using the Turtle graphics library. The game allows the player to control a snake and navigate it around the screen to eat food and grow longer. The objective is to score as many points as possible without colliding with the walls or the snake's own body.

<h2 style="font-size: 32px;">Gameplay</h2>
When the game starts, you will see a window with a black background.
Control the snake using the arrow keys (Up, Down, Left, Right) to change its direction.
The snake will move continuously in the chosen direction.
The objective is to eat the food that appears randomly on the screen.
Each time the snake eats the food, it will grow longer, and your score will increase by one.
Avoid colliding with the walls or the snake's own body. If the snake collides, the game will end.
The game over screen will be displayed, showing your final score.

<h2 style="font-size: 32px;">Code Structure</h2>
The code for the Snake game is organized into multiple files:
<br/><br/>
<strong>main.py:</strong> This is the main file that initializes the game and handles the game loop.<br>
<strong>board.py:</strong> Contains the Board class, responsible for displaying the score and the game over message.<br>
<strong>food.py:</strong> Contains the Food class, responsible for generating and managing the food objects.<br>
<strong>snake.py:</strong> Contains the Snake class, responsible for creating and controlling the snake.<br>
<h2 style="font-size: 32px;">Class Documentation</h2>

<h3 style="font-size: 30px;">Board class</h3>
This class handles the scoreboard and game over screen.
<br/><br/>
<strong>Methods</strong>
<br/><br/>
<strong>__init__():</strong> Initializes the Board object. It sets up the turtle graphics for displaying the score at the top of the screen.<br>
<strong>update_score():</strong> Updates the score on the screen whenever the snake eats the food.<br>
<strong>game_over():</strong> Displays the game over message in the center of the screen.<br>


<h3 style="font-size: 30px;">Food class</h3>
This class represents the food that the snake needs to eat.
<br/><br/>
<strong>Methods</strong>  
<br/><br/>
<strong>__init__():</strong> Initializes the Food object. It sets up the turtle graphics for displaying the food as a colored circle at a random position on the screen.<br>  
<strong>eated():</strong> Handles the logic when the snake eats the food. It generates a new random position and changes the food's color.  
<h3 style="font-size: 30px;">Snake class</h3>
This class represents the snake controlled by the player.  
<br/><br/>
<strong>Methods</strong>  
<br/><br/>
<strong>__init__():</strong> Initializes the Snake object. It sets up the turtle graphics for the snake's head and creates the initial snake body segments.<br>
<strong>create_snake():</strong> Creates the initial snake body segments based on the start_snake_body list of positions.<br>
<strong>extend_snake(position, color):</strong> Extends the snake by adding a new body segment at the given position with the specified color.<br>
<strong>move():</strong> Moves the snake forward in the current direction. It updates the positions of each body segment based on the position of the previous segment.<br>
<strong>move_up():</strong> Changes the snake's direction to upward if it's not currently moving downward.<br>
<strong>move_down():</strong> Changes the snake's direction to downward if it's not currently moving upward.<br>
<strong>move_left():</strong> Changes the snake's direction to the left if it's not currently moving right.<br>
<strong>move_right():</strong> Changes the snake's direction to the right if it's not currently moving left.<br>
