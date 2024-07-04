import time
from turtle import Screen
from classes import *


#Set up the screen
screen = Screen()
screen.setup(1000, 650)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

#Declarations
left_paddle = Paddle((-490,0))
right_paddle = Paddle((480,0))
ball = Ball()
scoreboard_left=ScoreBoard((-275,280))
scoreboard_right=ScoreBoard((265,280))



screen.update()

screen.listen()
screen.onkeypress(fun=left_paddle.move_up, key='w')
screen.onkeypress(fun=left_paddle.move_down, key='s')

screen.onkeypress(fun=right_paddle.move_up, key='Up')
screen.onkeypress(fun=right_paddle.move_down, key='Down')

game_is_on=True

bonce_x = True
bonce_y = True

while game_is_on:

      time.sleep(0.1)
      screen.update()
      ball.move()
      scoreboard_left.clear()
      scoreboard_right.clear()
      scoreboard_left.write(f"Score:{scoreboard_left.score}", align="center", font=("", 25, "normal"))
      scoreboard_right.write(f"Score: {scoreboard_right.score}", align="center", font=("", 25, "normal"))
      #Borders collision

      if ball.ycor()>=300 or ball.ycor()<=-300:
          ball.bounce_y()

      #Paddle collision
      if ball.distance(right_paddle)<50 and ball.xcor()>445 and bonce_x:
            ball.bounce_x()
            bonce_x=False
            bonce_y=True

      if ball.distance(left_paddle)<50 and ball.xcor()<-445 and bonce_y:
            ball.bounce_x()
            bonce_y=False
            bonce_x=True

      #The ball misses the paddle

      #Right side miss
      if ball.xcor()>505:
            ball.reset_position()
            ball.bounce_x()
            scoreboard_left.score+=1
            bonce_x=True
            bonce_y=True
      #Left side miss
      if ball.xcor() <-505 :
            ball.reset_position()
            ball.bounce_x()
            scoreboard_right.score += 1
            bonce_x = True
            bonce_y = True














screen.exitonclick()



