### Create a snake game in which the player is trying to schieve the highest score, if the snake hits the wall, the game is over
# import modueles
import turtle
import random
import time

# snake tail
snake_tail = []
score = 0
delay = 0.2
high_score = 0

# Create the screen
wn = turtle.Screen()
wn.bgcolor("green")
wn.title("Hungry Snake Game")
wn.setup(width=600, height=600)
wn.tracer(0)


# score box
score_printer = turtle.Turtle()
score_printer.shape("circle")
score_printer.color("white")
score_printer.penup()
score_printer.goto(0, 260)
score_printer.hideturtle()  # this function hides that little arrow showing up in the previous version of the game
score_printer.write("Score: 0  High Score:0", align="center", font=("italic", 24, "normal"))


# Create the Snake's head/start
head = turtle.Turtle()
head.shape("square")
head.color("Yellow")
head.penup()
head.direction = "stop"

# create the food
food = turtle.Turtle()
colors = random.choice(['red', 'purple', 'brown'])
shapes = random.choice(['circle', 'triangle', ])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 40)


# Define the movements and set the directions
def move_up():
    # This if statement will basically avoid the snake to run over itself
    # So if you are moving up, you cannot move down until you turn either left or right and then move down
    if head.direction != "down":
        head.direction = "up"


def move_down():
    if head.direction != "up":
        head.direction = "down"


def move_right():
    if head.direction != "left":
        head.direction = "right"


def move_left():
    if head.direction != "right":
        head.direction = "left"


# Snake Speed (Donnie)
speed = input("Press e for easy mode. Press h for hardcore mode: ")
if speed == "e":
    speed = 20
if speed == "h":
    speed = 30


def move():

    if head.direction == "up":
        y = head.ycor()
        head.sety(y + speed)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - speed)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + speed)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - speed)


# call the functions
wn.listen()
wn.onkeypress(move_up, "w")
wn.onkeypress(move_down, "s")
wn.onkeypress(move_right, "d")
wn.onkeypress(move_left, "a")


# main loop
while True:
    wn.update()
    def reset_score(seq):
        global score
        time.sleep(0.5)  # the snake freezes for a moment when hitting a wall then the game resets
        head.goto(0, 0)
        head.direction = "stop"
        score = 0
        for seq in snake_tail:
            seq.goto(1000, 1000)
        score = 0
        score_printer.clear()
        score_printer.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("italic", 24, "normal"))
        snake_tail.clear()
    # reset the game when the head hits the wall
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        reset_score("body_parts")

    # create a statement that when the head touches the food, the food should
    # appear randomly somewhere else on the screen
    if head.distance(food) < speed:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        new_tail = turtle.Turtle()
        new_tail.speed(0)
        new_tail.shape("square")
        new_tail.color("black")
        new_tail.penup()
        snake_tail.append(new_tail)
        # add to score when the snake eats food(when the head touches the food)
        score += 10
        if score > high_score:
            high_score = score
        score_printer.clear()
        score_printer.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("italic", 24, "normal"))


    # Move the  last body part, first in reverse
    for index in range(len(snake_tail)-1, 0, -1):
        x = snake_tail[index-1].xcor()
        y = snake_tail[index-1].ycor()
        snake_tail[index].goto(x, y)
    # Move body part 0 to where the head is
    if len(snake_tail) > 0:
        x = head.xcor()
        y = head.ycor()
        snake_tail[0].goto(x, y)
    move()

    # reset the game when the head touches the body
    for snake_tails in snake_tail:
        if snake_tails.distance(head) < speed:
            reset_score("snake_tails")
    wn.update()
    time.sleep(delay)

wn.mainloop()

