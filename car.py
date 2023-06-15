from turtle import Turtle, Screen
import random
screen = Screen()
#Define Car
class Car(Turtle):
    def __init__(self):
        super().__init__()
        colors = ["red", "blue", "green", "orange", "purple", "pink", "yellow", "brown", "black", "white"]
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color(colors[random.randint(0,len(colors)-1)])
        self.penup()
        
        
        
    def initialize_car(self,y):
        WIDTH = 280
        self.goto(460,y)
        
        
        
    def move(self):
        self.goto(self.xcor()-20,self.ycor())
        
        
        
    def delete_car(self):
        self.clear()
        del self
        
        
    
        
        
        
    
    