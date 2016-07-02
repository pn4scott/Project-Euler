# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number = random.randint(0,100)
    global num_of_guess_100
    num_of_guess_100 = 7

    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    print "Range 0 - 100\n"
    global secret_number
    global num_of_guess_100
    num_of_guess_100 = 7
    secret_number = random.randrange(0,100)
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    print "Range 0 - 1000\n"
    global num_of_guess_1000 
    num_of_guess_1000 = 10
    global secret_number
    secret_number = random.randrange(0,1000)

    
def input_guess(guess):
    # main game logic goes here	
    global secret_number, num_of_guess_100, num_of_guess_1000
    guess = int(guess)
    print "Player guessed", guess
    
     #compares guess with secret number
    if secret_number == guess:
        print "Correct, you win!\n"
        if num_of_guess_100 >= 0:
            range100()
        elif num_of_guess_1000 >= 0:
            range1000()
    elif secret_number > guess:
        print "Higher"
    elif secret_number < guess:
        print "Lower"
    
    #decrement code for guesses in range 0-100
    if int(guess) in range(0,100):
        num_of_guess_100 -= 1
        print "Guesses left", num_of_guess_100, "\n"
        
        #resetting after using all guesses
        if num_of_guess_100 == 0:
            print "New game begins"
            range100()
        
    #decrement code for guesses in range 0-1000
    elif int(guess) in range(0,1000):
        num_of_guess_1000 -= 1
        print "Guesses left", num_of_guess_1000, "\n"
        
        #resetting after using all guesses
        if num_of_guess_1000 == 0:
            print "New Game begins"
            range1000()
    

# create frame
frame = simplegui.create_frame("Guess the number!", 200, 200)

# register event handlers for control elements and start frame
frame.add_input("Input guess:", input_guess, 100)
frame.add_button("Range is [0,100)", range100, 150)
frame.add_button("Range is [0,1000)", range1000, 150)

# call new_game 
new_game()

