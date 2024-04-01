from turtle import Screen, Turtle
from Paddle import Paddle
from ball import Ball
import time

def main():
    global screen
    screen = Screen()
    screen.clear()
    screen.bgcolor('black')
    screen.setup(width=800, height=600)
    screen.tracer(0)

    right_p = Paddle((350, 0))
    right_l = Paddle((-350, 0))
    ball = Ball()

    screen.listen()
    screen.onkey(right_l.go_up, "w")
    screen.onkey(right_l.go_down, "s")
    screen.onkey(right_p.go_up, "Up")
    screen.onkey(right_p.go_down, "Down")

    game_is_on = True
    while game_is_on:
        time.sleep(0.001)
        screen.update()
        ball.move()
    
    
        # Detect collision with screen
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
            
        
        # Detect collision with paddles
        if ball.distance(right_p) < 40 or ball.distance(right_l) < 40:
            ball.bounce_x()
            
    
        if ball.xcor() > 380 or ball.xcor() < -380:
            game_is_on = False
            
    
            
    screen.clear()
    write()
    screen.onclick(lambda x, y: main())
    
    screen.mainloop()
    
    #Start()
    
    
    
def write():
    screen.bgcolor('black')
    button = Turtle()
    button.color("white")
    button.penup()
    button.hideturtle()
    button.goto(0, -70)
    button.write("Start", align='center', font=("Courier", 80, "normal"))
    #button.onclick(lambda x, y: main())
    
    

def Start():
    screen.bgcolor('black')
    button = Turtle()
    button.shape("square")
    button.color("red")
    button.shapesize(stretch_wid=4, stretch_len=16)
    button.penup()
    button.goto(0, 0)
    #button.write(write(), align='center', font=("Courier 20 normal"))
    button.onclick(lambda x, y: main())
    
    screen.mainloop()
    
if __name__ == "__main__":
    main()
