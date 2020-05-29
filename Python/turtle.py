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
