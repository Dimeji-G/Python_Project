from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from Score_Board import ScoreBoard

screen = Screen()
screen.setup(width=500, height = 500)
screen.bgcolor("black")
screen.title("Dimroid -- Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
  screen.update()
  time.sleep(0.09)

  snake.move()

#Detect collision with food 
  if snake.head.distance(food) < 15:
    snake.extend()
    food.refresh()

    scoreboard.increase_score()

#Detect collison with wall
  if snake.head.xcor() > 250 or snake.head.xcor() < -250 or snake.head.ycor() > 250 or snake.head.ycor() < -240:
    scoreboard.reset()
    snake.reset()

#Detect collison with tail
#if the head collides with any segment of the tail
  for segment in snake.segments[1:]:
    if segment == snake.head:
      pass
    elif snake.head.distance(segment) < 10:
       scoreboard.reset()
       snake.reset()
       
screen.exitonclick()
