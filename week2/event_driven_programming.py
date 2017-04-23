### Event Driven Programming ###

# This is an example of a simple event-driven program that is written to run in CodeSkulptor.

# CodeSkulptor GUI module
import simplegui

# SimpleGUITk is a wrapper for the CodeSkulptor SimpleGUI API using TkInter.
# https://pypi.python.org/pypi/SimpleGUITk
# Uncomment the next line and comment out 'import simplegui' above to run this program locally.
# import simpleguitk as simplegui

# Event Handler
def tick():
    print "tick!"

# Register Handler
timer = simplegui.create_timer(1000, tick)

# Start timer
timer.start()

# This program has no stop condition and will print "tick!" every second until it is interrupted.
# If this makes you nervous, there is a timer.stop() command that can be used.
# To stop this program in CodeSkulptor, hit the reset button.
# If you are running this program locally, use the control-c keyboard interrupt.
