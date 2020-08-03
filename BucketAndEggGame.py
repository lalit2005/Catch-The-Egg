import turtle
import random
import time
import pyglet

def cracksound() :
    music = pyglet.resource.media('EggCrackClip.wav')
    music.play()

def caughtsound() :
    music = pyglet.resource.media('CaughtSound.wav')
    music.play()

win = turtle.Screen()
win.tracer(0)
win.bgcolor("light blue")
win.setup(width = 800, height= 600)
win.title("Catch The Egg by Lalit")

# egg
egg=turtle.Turtle()
egg.penup()
egg.color("light yellow")
egg.speed(0)
egg.shape("circle")
egg.shapesize(stretch_len=1, stretch_wid=1.4)
egg.goto(0, 280)

# field
field = turtle.Turtle()
field.penup()
field.color("green")
field.goto(0,-300)
field.shape("square")
field.shapesize(stretch_len=40, stretch_wid=10)

# Bucket
bucket = turtle.Turtle()
bucket.penup()
bucket.goto(0, -180)
bucket.color("brown")
bucket.shape("square")
bucket.shapesize(stretch_len=3, stretch_wid=2)

balldy = 2.8



# Egg falling after being catched or left
def eggrenew():
    x = random.randint(-380, 380)
    y = 280
    egg.goto(x, y)

def ballfall():
    egg.sety( egg.ycor() - balldy )

def bucketleft() :
    bucket.setx(bucket.xcor() - 20)

def bucketright() :
    bucket.setx( bucket.xcor() + 20)

win.listen()
win.onkey(bucketleft, "a")
win.onkey(bucketright, "l")

score = 0

# losing announcer
lostann = turtle.Turtle()
lostann.penup()
lostann.color("red")
lostann.goto(0,0)
lostann.hideturtle()

# Scoreboard
scoreboard = turtle.Turtle()
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.color("black")
scoreboard.goto(0, 260)
scoreboard.write(f"-- Score : {score} -- ", align="center", font=("Courier",20,"normal"))

while True :
    win.update()

    # Check if falling in bucket
    if egg.ycor() < -235 and bucket.xcor() - 20 < egg.xcor() and bucket.xcor() + 20 > egg.xcor() :
        caughtsound()
        score = score + 1
        scoreboard.clear()
        scoreboard.write(f"-- Score : {score} -- ", align="center", font=("Courier",20,"normal"))
        eggrenew()

    # Falling of egg
    ballfall()

    # Checking ground
    if egg.ycor() < -270 :
        score = score - 1
        cracksound()
        scoreboard.clear()
        scoreboard.write(f"-- Score : {score} -- ", align="center", font=("Courier",20,"normal"))
        eggrenew()

    if score == -5 :
        lostann.write("You Lost !!!!",align="center",font=("courier",100,"underline"))
        time.sleep(3)
        quit()

    elif score == 10 :
        lostann.write("You Won !!!!",align="center",font=("courier",100,"underline"))
        time.sleep(3)
        quit()