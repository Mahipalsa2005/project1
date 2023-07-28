from sketchpy import library as lib
import turtle

# Create an RDJ object from the sketchpy library
obj = lib.rdj()

# Set  turtle screen
screen = turtle.Screen()
screen.setup(800, 800)
screen.title("RDJ Sketch")

# Create a turtle to draw RDJ digram
t = turtle.Turtle()

# Function to draw RDJ's face using the sketchpy library
def draw_rdj():
    for instruction in obj.draw():
        action, value = instruction
        if action == 'PENDOWN':
            t.pendown()
        elif action == 'PENUP':
            t.penup()
        elif action == 'MOVE':
            t.goto(value)
        elif action == 'SETHEADING':
            t.setheading(value)
        elif action == 'CIRCLE':
            t.circle(value)
        elif action == 'DOT':
            t.dot(5)
        elif action == 'FILL':
            t.fillcolor(value)
            t.begin_fill()
        elif action == 'ENDFILL':
            t.end_fill()
        elif action == 'COLOR':
            t.color(value)

draw_rdj()


