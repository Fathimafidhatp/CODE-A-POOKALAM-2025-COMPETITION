import turtle
import math


screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.title("Pookalam")
screen.bgcolor("#f0f0f0") 
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def get_pos(radius, angle_degrees):
    """Calculates x, y coordinates from a radius and angle in degrees."""
    angle_radians = math.radians(angle_degrees)
    x = radius * math.cos(angle_radians)
    y = radius * math.sin(angle_radians)
    return x, y


def draw_background_rings():
    """Draws the outermost solid rings that form the border."""

    t.penup()
    t.goto(0, -320)
    t.pendown()
    t.pencolor("#9A2A2A")
    t.pensize(20)
    t.circle(320)
    t.pensize(1)

    t.penup()
    t.goto(0, -300)
    t.pendown()
    t.color("#FADADD")
    t.begin_fill()
    t.circle(300)
    t.end_fill()

def draw_outer_pattern_ring():
    """Draws the checkered ring of yellow and red triangles."""
    colors = ["#FFD700", "#D22B2B"] # Yellow, Red
    for i in range(12):
        p1 = get_pos(180, i * 30)
        p2 = get_pos(300, i * 30)
        p3 = get_pos(240, i * 30 + 15)
        p4 = get_pos(180, (i + 1) * 30)
        p5 = get_pos(300, (i + 1) * 30)

        t.penup()
        t.goto(p1)
        t.pendown()
        t.color(colors[0])
        t.begin_fill()
        t.goto(p2)
        t.goto(p3)
        t.goto(p1)
        t.end_fill()

        t.penup()
        t.goto(p4)
        t.pendown()
        t.color(colors[1])
        t.begin_fill()
        t.goto(p5)
        t.goto(p3)
        t.goto(p4)
        t.end_fill()

def draw_middle_pattern_ring():
    """Draws the ring with red, black, green, and yellow triangles."""
    colors = ["#D22B2B", "#000000", "#006400", "#FFD700"]
    for i in range(12):

        p1 = get_pos(110, i * 30 + 15)
        p2 = get_pos(180, i * 30)
        p3 = get_pos(180, (i + 1) * 30)

        t.penup()
        t.goto(p1)
        t.pendown()
        t.color(colors[i % 4])
        t.begin_fill()
        t.goto(p2)
        t.goto(p3)
        t.goto(p1)
        t.end_fill()

def draw_inner_star_pattern():
    """Draws the green and white 12-pointed star pattern."""

    t.penup()
    t.goto(0, -110)
    t.pendown()
    t.color("#006400") # Dark Green
    t.begin_fill()
    t.circle(110)
    t.end_fill()

    for i in range(12):

        p1 = get_pos(45, i * 30)
        p2 = get_pos(110, i * 30 - 15)
        p3 = get_pos(110, i * 30 + 15)

        t.penup()
        t.goto(p1)
        t.pendown()
        t.color("white")
        t.begin_fill()
        t.goto(p2)
        t.goto(p3)
        t.goto(p1)
        t.end_fill()

def draw_center_flower():
    """Draws the central red circle and the pink flower."""

    t.penup()
    t.goto(0, -45)
    t.pendown()
    t.color("#C04040") 
    t.begin_fill()
    t.circle(45)
    t.end_fill()
r
    t.penup()
    t.home()
    t.pendown()
    t.color("#F08080")
    for i in range(8):
        t.setheading(i * 45)
        t.begin_fill()

        t.circle(30, 80)
        t.left(100)
        t.circle(30, 80)
        t.end_fill()


draw_background_rings()
draw_outer_pattern_ring()
draw_middle_pattern_ring()
draw_inner_star_pattern()
draw_center_flower()

screen.update()

screen.exitonclick()