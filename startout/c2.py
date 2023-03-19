#!/usr/bin/env python3

import turtle

# turtle.showturtle()

turtle.hideturtle()
turtle.pendown()
turtle.pencolor("black")
turtle.fillcolor("cyan")
turtle.begin_fill()
turtle.goto(120, 120)
turtle.goto(200, -100)
turtle.goto(0, 0)
turtle.end_fill()
turtle.penup()

turtle.goto(-200, 0)
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
turtle.penup()

turtle.done()
