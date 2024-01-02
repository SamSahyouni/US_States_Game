# create a class that takes inputs and writes the state

from turtle import  Turtle,Screen
FONT = ("Courier", 12, "normal")

class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def update_map(self,coordinates,state):
        self.goto(coordinates)
        self.write(align="center",font=FONT,arg=state)

