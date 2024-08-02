from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Read documentation. Used to turn off animation


snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
score = 0
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    scoreboard.display_score(score)
    # Detect collision with food
    if snake.head.distance(food) < 15:
        score += 1
        scoreboard.display_score(score)
        food.refresh()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 295 or snake.head.ycor() > 300 or snake.head.xcor() < -295 or snake.head.ycor() < -300:
        game_is_on = False
        scoreboard.end_game(score)

    # Detect collision with tail
    for segment in snake.all_snakes[1:]:
        if snake.head.distance(segment) < 5:
            game_is_on = False
            scoreboard.end_game(score)
screen.exitonclick()
