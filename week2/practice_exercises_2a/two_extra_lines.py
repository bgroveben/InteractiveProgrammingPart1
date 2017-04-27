# 4.

# Open a frame

###################################################
# Open frame
# Student should add code where relevant to the following.

# import simplegui

# https://pypi.python.org/pypi/SimpleGUITk
# Uncomment the next line and comment out 'import simplegui' above to run this program locally.
import simpleguitk as simplegui

message = "My first frame!"

# Handler for mouse click.
def click():
    print message

# Create a frame and assign callbacks to event handlers.
frame = simplegui.create_frame("My first frame", 100, 200)
frame.add_button("Click me", click)
frame.start()
