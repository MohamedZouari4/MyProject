import turtle

wind = turtle.Screen()
wind.title("Ping Pong BY ZouZou")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)

start_screen = turtle.Turtle()
start_screen.speed(0)
start_screen.color("white")
start_screen.penup()
start_screen.hideturtle()
start_screen.goto(0, 100)
start_screen.write("Welcome to Ping Pong!", align="center", font=("Courier", 24, "normal"))
start_screen.goto(0, 50)
start_screen.write("Press SPACE to Start", align="center", font=("Courier", 18, "normal"))

# center line
center_line = turtle.Turtle()
center_line.speed(0)
center_line.shape("square")
center_line.color("white")
# width => 500px = 25 * 20px default
center_line.shapesize(stretch_len=.1, stretch_wid=25)
center_line.penup()
center_line.goto(0, 0)

# racket 1
raket1 = turtle.Turtle()
raket1.speed(0)
raket1.shape("square")
raket1.color("blue")
raket1.shapesize(stretch_wid=5, stretch_len=1)
raket1.penup()
raket1.goto(-350, 0)

# racket 2
raket2 = turtle.Turtle()
raket2.speed(0)
raket2.shape("square")
raket2.color("red")
raket2.shapesize(stretch_wid=5, stretch_len=1)
raket2.penup()
raket2.goto(350, 0)

# ball
kora = turtle.Turtle()
kora.speed(0)
kora.shape("square")
kora.color("white")
kora.penup()
kora.goto(0, 0)
kora.dx = 0.1
kora.dy = 0.1

# score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1 = 0 Player 2 = 0", align="center", font=("courier", 24, "normal"))

# function
def raket1_up():
    y = raket1.ycor()
    y += 20
    raket1.sety(y)

def raket1_down():
    y = raket1.ycor()
    y -= 20
    raket1.sety(y)

def raket2_up():
    y = raket2.ycor()
    y += 20
    raket2.sety(y)

def raket2_down():
    y = raket2.ycor()
    y -= 20
    raket2.sety(y)

def update_score():
    score.clear()
    score.write("Player 1 = {} Player 2 = {}".format(score1, score2), align="center", font=("courier", 24, "normal"))

def start_game():
    start_screen.clear()
    # Bind the keyboard keys
    wind.listen()
    wind.onkeypress(raket1_up, "z")
    wind.onkeypress(raket1_down, "s")
    wind.onkeypress(raket2_up, "Up")
    wind.onkeypress(raket2_down, "Down")

# Bind the spacebar key to start the game
wind.listen()
wind.onkeypress(start_game, "space")

# Main game loop
while True:
    wind.update()

    # move the ball
    kora.setx(kora.xcor() + kora.dx)
    kora.sety(kora.ycor() + kora.dy)

    # border check
    if kora.ycor() > 290 or kora.ycor() < -290:
        kora.dy *= -1

    if kora.xcor() > 390:
        kora.goto(0, 0)
        kora.dx *= -1
        score1 += 1
        update_score()

    if kora.xcor() < -390:
        kora.goto(0, 0)
        kora.dx *= -1
        score2 += 1
        update_score()

    # racket and ball collisions
    if (kora.xcor() > 340 and kora.xcor() < 350) and (kora.ycor() < raket2.ycor() + 50 and kora.ycor() > raket2.ycor() - 50):
        kora.setx(340)
        kora.dx *= -1

    elif (kora.xcor() < -340 and kora.xcor() > -350) and (kora.ycor() < raket1.ycor() + 50 and kora.ycor() > raket1.ycor() - 50):
        kora.setx(-340)
        kora.dx *= -1
