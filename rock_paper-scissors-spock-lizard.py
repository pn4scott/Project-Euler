# Rock-paper-scissors-lizard-Spock template


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
import random

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        "Error; Enter rock, Spock, paper, lizard, scissors."

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return 'Error; integer not in range 0 to 4.'

    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    
    
    # print a blank line to separate consecutive games
    print '\n'
    # print out the message for the player's choice
    print "Player chooses", player_choice
    # convert the player's choice to player_number using the function name_to_number()
    name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,4)
    # convert comp_number to comp_choice using the function number_to_name()
    number_to_name(comp_number)
    # print out the message for computer's choice
    print "Computer chooses", number_to_name(comp_number)
    # compute difference of comp_number and player_number modulo five
    comp_diff = (name_to_number(player_choice) - comp_number) % 5
    # use if/elif/else to determine winner, print winner message
    if comp_diff == 1 or comp_diff == 2:
        return "Player wins!"
    elif comp_diff == 3 or comp_diff == 4:
        return "Computer wins!"
    elif comp_diff == 0:
        return "None wins"
    elif comp_diff == -1:
        comp_diff = comp_diff + 5
        if comp_diff == 4:
            return "computer wins"
    else:
        return "Error"

# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
print rpsls("rock")
print rpsls("Spock")
print rpsls("paper")
print rpsls("lizard")
print rpsls("scissors")

# always remember to check your completed program against the grading rubric

