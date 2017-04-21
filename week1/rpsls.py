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
    """
    (str) -> int

    Convert the string name into a number between 0 and 4 as described in the comments above.

    >>> name_to_number("rock")
    0
    >>> name_to_number("Spock")
    1
    >>> name_to_number("paper")
    2
    >>> name_to_number("lizard")
    3
    >>> name_to_number("scissors")
    4
    >>> name_to_number("invalid")
    'Sorry, that input is invalid. Please choose rock, paper, scissors, lizard, or Spock.'
    """
    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Sorry, that input is invalid. Please choose rock, paper, scissors, lizard, or Spock."



def number_to_name(number):
    """
    (int) -> str

    Convert a number in the range 0 to 4 into its corresponding name as a string.

    >>> number_to_name(0)
    'rock'
    >>> number_to_name(1)
    'Spock'
    >>> number_to_name(2)
    'paper'
    >>> number_to_name(3)
    'lizard'
    >>> number_to_name(4)
    'scissors'
    >>> number_to_name(-1)
    'Sorry, that is an invalid number. Please choose a number between 0 and 4.'
    >>> number_to_name(5)
    'Sorry, that is an invalid number. Please choose a number between 0 and 4.'
    """
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "Sorry, that is an invalid number. Please choose a number between 0 and 4."


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


if __name__=="__main__":
    import doctest
    print doctest.testmod()
