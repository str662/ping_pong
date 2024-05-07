import turtle
from random import choice, randint

win = turtle.Screen()
win.title('Ping Pong')
win.setup(width=1.0, height=1.0)
win.bgcolor('black')
win.tracer(1.8)

border = turtle.Turtle()
border.speed(10)
border.color('white')
border.begin_fill()
border.goto(-500,300)
border.goto(500,300)
border.goto(500,-300)
border.goto(-500,-300)
border.goto(-500,300)
border.end_fill()

border.goto(0, 300)
border.color('black')
border.goto(0, -300)
border.hideturtle()

player1 = turtle.Turtle()
player1.color('black')
player1.shape('square')
player1.shapesize(stretch_wid=5, stretch_len=1)
player1.penup()
player1.goto(-450, 0)

player2 = turtle.Turtle()
player2.color('black')
player2.shape('square')
player2.shapesize(stretch_wid=5, stretch_len=1)
player2.penup()
player2.goto(450, 0)

FONT = ("Arial", 45)
score1 = 0
s1 = turtle.Turtle(visible=False)
s1.color('white')
s1.penup()
s1.setposition(-200,300)
s1.write(score1, font=FONT)

score2 = 0
s2 = turtle.Turtle(visible=False)
s2.color('white')
s2.penup()
s2.setposition(200,300)
s2.write(score2, font=FONT)

def up():
    y = player1.ycor() + 10
    if y > 250:
        y = 250
    player1.sety(y)

def down():
    y = player1.ycor() - 10
    if y < -250:
        y = -250
    player1.sety(y)

def up2():
    y = player2.ycor() + 10
    if y > 250:
        y = 250
    player2.sety(y)

def down2():
    y = player2.ycor() - 10
    if y < -250:
        y = -250
    player2.sety(y)

ball = turtle.Turtle()
ball.shape('circle')
ball.speed(0)
ball.color('black')
ball.dx = 3
ball.dy = -3
ball.penup()


win.listen()
win.onkeypress(up, 'w')
win.onkeypress(down, 's')
win.onkeypress(up2, 'Up')
win.onkeypress(down2, 'Down')


while True:

    win.update()

    ball.setx(ball.xcor() +   ball.dx)
    ball.sety(ball.ycor() +   ball.dy)

    if ball.ycor() >= 290:
        ball.dy = -ball.dy

    if ball.ycor() <= -290:
        ball.dy = -ball.dy 

    if ball.xcor() >= 490:
        score2 += 1
        s2.clear()
        s2.write(score2, font=FONT)
        ball.goto(0,randint(-150,150))
        ball.dx = choice([-4, -3, -2, 2, 3, 4])
        ball.dy = choice([-4, -3, -2, 2, 3, 4])  

    if ball.xcor() <= -490:
        score1 += 1
        s1.clear()
        s1.write(score1, font=FONT)
        ball.goto(0,randint(-150,150)) 
        ball.dx = choice([-4, -3, -2, 2, 3, 4])
        ball.dy = choice([-4, -3 ,-2, 2, 3, 4])
    
    if ball.ycor() >= player1.ycor() -50 and ball.ycor() <= player1.ycor() + 50 \
    and ball.xcor() >= player1.xcor() - 5 and ball.xcor() <= player1.xcor() + 5:
        ball.dx = -ball.dx

    if ball.ycor() >= player2.ycor() -50 and ball.ycor() <= player2.ycor() + 50 \
    and ball.xcor() >= player2.xcor() - 5 and ball.xcor() <= player2.xcor() + 5:
        ball.dx = -ball.dx




win.mainloop()