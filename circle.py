import turtle
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Drawing Lines Practice")

my_turtle = turtle.Turtle()
my_turtle.pensize(2)
my_turtle.color("brown")
my_turtle.fillcolor("yellow")
my_turtle.begin_fill()
my_turtle.circle(100)
my_turtle.end_fill()

my_turtle.hideturtle()
turtle.done()
