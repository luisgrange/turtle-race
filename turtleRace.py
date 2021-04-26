import turtle
import random as rd

#random velocity
sec_random = rd.SystemRandom()

randVelA = sec_random.uniform(0.1, 0.8)
randVelB = sec_random.uniform(0.1, 0.8)
randVelC = sec_random.uniform(0.1, 0.8)

wn = turtle.Screen()
wn.title('Turtle racing')
wn.bgcolor("green")
wn.setup(width=800, height=500)
wn.tracer(0)

# arrival line
line = turtle.Turtle()
line.shape("square")
line.color("white")
line.shapesize(stretch_wid=25, stretch_len=1)
line.speed(0)
line.penup()
line.goto(290, 0)

#turtle A:
paddle_turtleA = turtle.Turtle()
paddle_turtleA.speed(0)
paddle_turtleA.shape('turtle')
paddle_turtleA.color('blue')
paddle_turtleA.penup()
paddle_turtleA.goto(-360, 0)

#turtle B:
paddle_turtleB = turtle.Turtle()
paddle_turtleB.speed(0)
paddle_turtleB.shape('turtle')
paddle_turtleB.color('pink')
paddle_turtleB.penup()
paddle_turtleB.goto(-360, 35)

#turtle C:
paddle_turtleC = turtle.Turtle()
paddle_turtleC.speed(0)
paddle_turtleC.shape('turtle')
paddle_turtleC.color('purple')
paddle_turtleC.penup()
paddle_turtleC.goto(-360, -35)

#write who is the winner
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.color("white")
pen.goto(0, 0)
pen.hideturtle()

#movements
paddle_turtleA.dx = randVelA
paddle_turtleA.dy = 0

paddle_turtleB.dx = randVelB
paddle_turtleB.dy = 0

paddle_turtleC.dx = randVelC
paddle_turtleC.dy = 0

#main loop
while True:
    wn.update()

    paddle_turtleA.setx(paddle_turtleA.xcor() + paddle_turtleA.dx)
    paddle_turtleB.setx(paddle_turtleB.xcor() + paddle_turtleB.dx)
    paddle_turtleC.setx(paddle_turtleC.xcor() + paddle_turtleC.dx)

    if paddle_turtleA.xcor() > 310:
        paddle_turtleA.dx = 0
        paddle_turtleB.dx = 0
        paddle_turtleC.dx = 0
        pen.write("Blue turtle wins", align="center", font=("Courier", 24, "normal"))

    if paddle_turtleB.xcor() > 310:
        paddle_turtleA.dx = 0
        paddle_turtleB.dx = 0
        paddle_turtleC.dx = 0
        pen.write("Pink turtle wins", align="center", font=("Courier", 24, "normal"))

    if paddle_turtleC.xcor() > 310:
        paddle_turtleA.dx = 0
        paddle_turtleB.dx = 0
        paddle_turtleC.dx = 0
        pen.write("Purple turtle wins", align="center", font=("Courier", 24, "normal"))