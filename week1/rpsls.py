# Rock-paper-scissors-lizard-Spock template
# Go to:
# https://www.coursera.org/learn/interactive-python-1/supplement/ijRP5/mini-project-description
# for a description of the mini-project.
# There is also a practice mini-project called mystical_octosphere at:
# https://www.coursera.org/learn/interactive-python-1/supplement/S0NFz/practice-mini-project-mystical-octosphere-optional
# that is in the file mystical_octosphere.py in this directory.


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    pass

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    pass

    # convert number to a name using if/elif/else
    # don't forget to return the result!


def rpsls(player_choice):
    # delete the following pass statement and fill in your code below
    pass

    # print a blank line to separate consecutive games

    # print out the message for the player's choice

    # convert the player's choice to player_number using the function name_to_number()

    # compute random guess for comp_number using random.randrange()

    # convert comp_number to comp_choice using the function number_to_name()

    # print out the message for computer's choice

    # compute difference of comp_number and player_number modulo five

    # use if/elif/else to determine winner, print winner message


# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
