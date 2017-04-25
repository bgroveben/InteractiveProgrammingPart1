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

### Checklist from the class notes with an example:
# This program will count up one number every second and reset to 0 when the button is clicked.
# It works in CodeSkulptor, but I can't get it to run locally yet, so I have some tinkering to do.

# SimpleGUI program template
# Import the module
import simplegui
# import simpleguitk as simplegui

# Define global variables (program state)
counter = 0

# Define "helper" functions
def increment():
    global counter
    counter = counter + 1

# Define event handler functions
def tick():
    increment()
    print counter

def buttonpress():
    global counter
    counter = 0

# Create a frame
frame = simplegui.create_frame("SimpleGUI Test", 100, 100)

# Register event handlers
timer = simplegui.create_timer(1000, tick)
frame.add_button("Click me!", buttonpress)

# Start frame and timers
frame.start()
timer.start()
