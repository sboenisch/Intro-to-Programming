import turtle
fred = turtle.Turtle()
fred.color("red")
fred.forward(100)
fred.right(135)
fred.forward(140)
fred.right(135)
fred.forward(100)

# for-Schleife
amy = turtle.Turtle()
amy.color("green")
for side in [1, 2, 3, 4]:
    amy.forward(100)
    amy.right(90)

# Pentagon
amy = turtle.Turtle()
amy.color("green")

for side in [1, 2, 3, 4, 5]:
    amy.forward(100)
    amy.right(72)

# Color assignment
p = "purple"
mary.color(p)

# Draw a house
import turtle

builder = turtle.Turtle()
builder.color("red")
builder.width(5)

# Copy the angles variable here!
angles = [-90, 0, 0, -90,
          135, 0, 0, 0,
          90, 0, 0, 0,
          135, -90, 0, 0,
          90, 0, 0, 0]

for angle in angles:
    # Turn right, then go forward 25.
    # (How far to turn?
    #  Use the angle variable!)
    builder.right(angle)
    builder.forward(25)


# Draw three red lines
amy = turtle.Turtle()

# Make the width thicker so that the line will be easier to see
amy.width(5)

# Move back without drawing anything
amy.penup()
amy.back(140)
amy.pendown()

# Draw three red lines, with space in between
amy.color("red")

for i in [1,2,3]:
    amy.forward(50)
    amy.penup()
    amy.forward(50)
    amy.pendown()

# Three nice squares
amy = turtle.Turtle()

# Make the width thicker so that the line will be easier to see
amy.width(5)

# Move back without drawing anything
amy.penup()
amy.forward(-140)
amy.pendown()

# Draw three shapes of different colors, with space in between
for prettycolor in ["red", "orange", "yellow"]:
  amy.color(prettycolor)
  for side in [1, 2, 3, 4]:
    amy.forward(50)
    amy.right(90)
  amy.penup()
  amy.forward(100)
  amy.pendown()

# Awesome drawing
t = turtle.Turtle()
t.color("cyan")

for side in range(20):
    t.speed(0)
    t.forward(10*side)
    t.right(120)

# Functions
jack = turtle.Turtle()
jack.color("yellow")

def draw_square():
    for side in range(4):
        jack.forward(100)
        jack.right(90)

draw_square()

# Flower
# Write a function here that creates a
# turtle and draws a shape with it.
def triangle_boogie(color, start):
  t = turtle.Turtle()
  t.color(color)
  t.speed(0)
  t.width(5)
  t.right(start)
  for shape in range(6):
    for side in range(3):
      t.forward(100)
      t.right(120)
    t.right(15)
  t.hideturtle()

# Call the function multiple times.
triangle_boogie("red", 0)
triangle_boogie("orange", 120)
triangle_boogie("blue", 240)

# Ballons
def balloon(t, color):
    t.speed(0)
    t.color(color)

    # Draw balloon body.
    for side in range(30):
        t.forward(10)
        t.left(12)

    # Draw balloon knot.
    t.right(60)
    for side in range(3):
        t.forward(10)
        t.right(120)

    # Draw balloon string.
    t.color("gray")
    t.right(30)
    t.forward(100)


t = turtle.Turtle()

t.penup()
t.back(100)
t.pendown()
balloon(t, "red")

t.penup()
t.home()
t.pendown()
balloon(t, "blue")

t.penup()
t.home()
t.forward(100)
t.pendown()
balloon(t, "purple")

t.hideturtle()

# One Object two names
romeo = turtle.Turtle()
montague = romeo

montague.color("red")
montague.width(5)

montague.forward(100)
montague.right(90)
montague.forward(100)
montague.right(90)
romeo.color("white")
montague.forward(100)
montague.right(90)
montague.forward(100)
montague.right(90)

# Draw a flower out of squares
def draw_square(some_turtle):
    for side in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)

romeo = turtle.Turtle()
romeo.color("violet")
romeo.speed(8)
for petal in range(6):
    draw_square(romeo)
    romeo.right(60)

romeo.hideturtle()

# Function practice
romeo = turtle.Turtle()
romeo.color("violet")
romeo.width(5)
romeo.speed(8)

def draw_square(some_turtle):
    for side in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_flower(some_turtle):
    for petal in range(6):
        draw_square(some_turtle)
        some_turtle.right(60)
        some_turtle.hideturtle()

draw_flower(romeo)

# Heart Drawing ♥
romeo = turtle.Turtle()
juliet = turtle.Turtle()

juliet.color("misty rose")
juliet.width(3)

romeo.color("violet")
romeo.width(3)

romeo_last_name = "montague"

romeo.left(40)
romeo.forward(100)
for side in range(185):
    romeo.forward(1)
    romeo.left(1)
romeo.hideturtle()

if romeo_last_name == "montague":
    juliet.left(140)
    juliet.forward(100)
    for side in range(185):
        juliet.forward(1)
        juliet.right(1)
    juliet.hideturtle()

# Modulo Operator
def bead(tur):
    tur.right(75)
    for _ in range(12):
        tur.forward(10)
        tur.left(30)
    tur.left(75)

t = turtle.Turtle()
t.speed(0)
t.width(2)

# Move to the left before starting.
t.penup()
t.back(200)
t.pendown()

# Draw ten beads.
for n in range(10):
    if n % 2 == 0:
        t.color("blue")
    else:
        t.color("red")
    bead(t)
    t.forward(40)

# Drawing stairs
amy = turtle.Turtle()
amy.color("red")

for step in range(6):
    amy.forward(50)
    if(step%2==0):
        amy.left(90)
    else:
        amy.right(90)

# Weird shapet = turtle.Turtle()
t.color("white")
t.width(1)
t.speed(0)
t.hideturtle()

def square(number):
    return number*number


for n in range(540):
    angle = square(n)
    t.right(angle + .5)
    t.forward(5)
