#! /usr/bin/env python3

# This program draws the stars of the Orion constellation

import turtle

# setup the window size
turtle.setup(500, 600)

# setup the turtle
turtle.penup()
turtle.hideturtle()

# create constants for the coordinates
LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 200
RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180
LEFT_BELTSTAR_X = -40
LEFT_BELTSTAR_Y = -20
MIDDLE_BELTSTAR_X = 0
MIDDLE_BELTSTAR_Y = 0
RIGHT_BELTSTAR_X = 40
RIGHT_BELTSTAR_Y = 20
LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180
RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -140

# draw the stars
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.dot()
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.dot()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.dot()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.dot()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.dot()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.dot()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
turtle.dot()

# display the star names
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y + 5)
turtle.write("Beteguese")
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y + 5)
turtle.write("Meissa")
turtle.goto(LEFT_BELTSTAR_X - 30, LEFT_BELTSTAR_Y)
turtle.write("Alnitak")
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y - 15)
turtle.write("Alnilam")
turtle.goto(RIGHT_BELTSTAR_X + 10, RIGHT_BELTSTAR_Y)
turtle.write("Mintaka")
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y - 15)
turtle.write("Saiph")
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y - 15)
turtle.write("Rigel")

# draw the lines
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.pendown()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.penup()
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.pendown()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.penup()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)

# keep the window open
turtle.done()
