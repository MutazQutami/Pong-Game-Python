from turtle import Turtle, Screen
import random

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=6,stretch_len=1)
        self.color('white')
        self.speed("fastest")
        self.penup()
        self.goto(position)

    def move_up(self):
        y=self.ycor()
        x=self.xcor()

        if y<250:
           self.goto(x,y+20)

    def move_down(self):
        y = self.ycor()
        x = self.xcor()

        if y > -250:
            self.goto(x, y - 20)


class Ball(Turtle):
  def __init__(self):
      super().__init__()
      self.shape("circle")
      self.color('white')
      self.speed("slowest")
      self.penup()
      self.x_move = 25
      self.y_move = 25


  def move(self):
     new_y=  self.ycor()+self.y_move
     new_x= self.xcor()+self.x_move
     self.goto(new_x,new_y)
  def bounce_y(self):
      self.y_move*=-1
  def bounce_x(self):
      self.x_move*=-1
  def reset_position(self):
      self.goto(0,0)

class ScoreBoard(Turtle):
    def __init__(self,position):
      super().__init__()
      self.shape("square")
      self.color("white")
      self.hideturtle()
      self.penup()
      self.goto(position)
      self.score=0

