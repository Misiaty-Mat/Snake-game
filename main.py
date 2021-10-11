from turtle import Screen
import time
from scoreboard import Scoreboard
from snake import Snake
from food import Food

# game setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Mateusz Miś - Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

# user inputs
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.update()


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 20:
        food.rand_location()
        snake.extend()
        scoreboard.increase_score(by_amount=1)
        scoreboard.update_scoreboard()

    # Wall collision detector
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    # tail collision detector
    for segment in snake.segments[1:]:
        # taking all segment apart from first one
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()


screen.exitonclick()
