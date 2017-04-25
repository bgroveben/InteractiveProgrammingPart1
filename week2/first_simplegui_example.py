### SimpleGUI Example Program ###

# CodeSkulptor GUI module
# import simplegui

# SimpleGUITk is a wrapper for the CodeSkulptor SimpleGUI API using TkInter.
# https://pypi.python.org/pypi/SimpleGUITk
# Uncomment the next line and comment out 'import simplegui' above to run this program locally.
import simpleguitk as simplegui

message = "Welcome!"

# Handler for mouse click.
def click():
    # https://docs.python.org/2/reference/simple_stmts.html#the-global-statement
    global message
    message = "Good job!"

# Handler to draw on canvas.
def draw(canvas):
    canvas.draw_text(message, [50,112], 36, "Red")

# Create a frame and assign callbacks to event handlers.
frame = simplegui.create_frame("Home", 300, 200)
frame.add_button("Click me", click)
frame.set_draw_handler(draw)

# Start the frame animation.
frame.start()


#!#! Program Structure for SimpleGUI Programs #!#!
### A 'Recipe' for building programs with SimpleGUI ###
# Seven Steps:
# 1. Define global variables (state).
# 2. Define helper functions.
# 3. Define classes.
# 4. Define event handlers.
# 5. Create a frame.
# 6. Register event handlers.
# 7. Start frame and (if any) timers.
