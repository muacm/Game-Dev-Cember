import turtle
import os
#import winsound

wn_height = 600
wn_width = 800

ball_speed = 0.1

win_score = 5

paddle_pos = ((wn_width/2)-50)

#Initialising window

wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("#000040")
wn.setup(width=wn_width, height=wn_height)
wn.tracer(0)

#Middle line
m_line = turtle.Turtle()
m_line.speed(0)
m_line.shape("square")
m_line.shapesize(stretch_len=0.1, stretch_wid=(wn_height/2)/10)
m_line.color("#F7EE01")
m_line.penup()
m_line.goto(0, 0)


#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_len=0.7, stretch_wid=5)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-paddle_pos, 0)


#Paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_len=0.7, stretch_wid=5)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(paddle_pos, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = ball_speed
ball.dy = ball_speed

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("retro_gaming/Retro Gaming.ttf", 20, "normal"))

#Scores
paddle_a.score = 0
paddle_b.score = 0

#Function

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)





def game_run():

    #Game run

    while True:
        wn.update()

        #Keyboard input
        wn.listen()
        wn.onkeypress(paddle_a_up, "w")
        wn.onkeypress(paddle_a_down, "s")

        wn.onkeypress(paddle_b_up, "Up")
        wn.onkeypress(paddle_b_down, "Down")


        #Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        #Paddle y-axis limit
        #Paddle a
        if paddle_a.ycor()>(wn_height/2)-50:
            paddle_a.sety((wn_height/2)-50)

        if paddle_a.ycor()<(-wn_height/2)+50:
            paddle_a.sety((-wn_height/2)+50)

        #Paddle b
        if paddle_b.ycor()>(wn_height/2)-50:
            paddle_b.sety((wn_height/2)-50)

        if paddle_b.ycor()<(-wn_height/2)+50:
            paddle_b.sety((-wn_height/2)+50)

        #Border check
        #Vertical borders
        if ball.ycor() > (wn_height/2)-10:
            ball.sety((wn_height/2)-10)
            ball.dy *= -1
            os.system("aplay bounce.wav -q&")
            #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


        if ball.ycor() < -((wn_height/2)-15):
            ball.sety(-((wn_height/2)-15))
            ball.dy *= -1
            os.system("aplay bounce.wav -q&")
            #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


        #Horizontal borders
        if ball.xcor() > (wn_width/2)-10:
            ball.setx(0)
            ball.sety(0)
            paddle_a.score+=1
            ball.dx=ball_speed
            ball.dy=ball_speed
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(paddle_a.score, paddle_b.score), align="center", font=("retro_gaming/Retro Gaming.ttf", 20, "normal"))

        if ball.xcor() < -((wn_width/2)-10):
            ball.setx(0)
            ball.sety(0)
            paddle_b.score+=1
            ball.dx=ball_speed
            ball.dy=ball_speed
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(paddle_a.score, paddle_b.score), align="center", font=("retro_gaming/Retro Gaming.ttf", 20, "normal"))

        #Collision check
        if((ball.xcor() < paddle_a.xcor()+10 and ball.xcor() > paddle_a.xcor()-10) and (ball.ycor() < paddle_a.ycor()+50 and ball.ycor() > paddle_a.ycor()-50)):
            ball.setx(paddle_a.xcor()+10)
            ball.dx *= -1
            ball.dx+=0.02
            ball.dy+=0.02
            os.system("aplay bounce.wav -q&")
            #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)



        if((ball.xcor() > paddle_b.xcor()-10 and ball.xcor() < paddle_b.xcor()+10) and (ball.ycor() < paddle_b.ycor()+50 and ball.ycor() > paddle_b.ycor()-50)):
            ball.setx(paddle_b.xcor()-10)
            ball.dx *= -1
            ball.dx-=0.02
            ball.dy-=0.02
            os.system("aplay bounce.wav -q&")
            #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


        if paddle_a.score>=win_score:
            wn.clear()
            paddle_a.score = 0
            wn.bgcolor("#000040")
            pen.goto(0,0)
            pen.write("GAME OVER\nPlayer A Wins", align="center", font=("retro_gaming/Retro Gaming.ttf", 50, "normal"))

        if paddle_b.score>=win_score:
            wn.clear()
            paddle_b.score = 0
            wn.bgcolor("#000040")
            pen.goto(0,0)
            pen.write("GAME OVER\nPlayer B Wins", align="center", font=("retro_gaming/Retro Gaming.ttf", 50, "normal"))

game_run()