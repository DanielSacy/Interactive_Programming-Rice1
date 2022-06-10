import simplegui
import random
import math

current = None
guesses = None

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global guesses
    if current == b1 : 
        secret_number = random.randrange(0,100)
        guesses = int(math.ceil(math.log(100, 2)))
        print('New Game! The range is [0, 100)')
    elif current == b2 : 
        secret_number = random.randrange(0,1000)
        guesses = int(math.ceil(math.log(1000, 2)))
        print('New Game! The range is [0, 1000)')
    else:
        secret_number = random.randrange(0,100)
        guesses = int(math.ceil(math.log(100, 2)))
        print('New Game! The range is [0, 100)')

    print 'Guesses Remaining:', guesses
    print(' ')
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global current
    current = b1
    new_game()
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global current
    current = b2
    new_game()
    
def input_guess(guess):
    # main game logic goes here
    global guesses
    guess = int(guess)
    print 'You guessed:', guess
    guesses -= 1
    if (guess != secret_number) and (guesses == 0) : 
        print('Wrong guess... I guess')
        print('Out of Guesses =[')
        print(' ')
        new_game()            
    elif guess < secret_number : 
        print('Higher')
        print 'Guesses Remaining:', guesses, '\n'
    elif guess > secret_number : 
        print('Lower')
        print 'Guesses Remaining:', guesses, '\n'
    else : 
        print('Correct!')
        print(' ')
        new_game()
        
# create frame
frame = simplegui.create_frame('Guess the Number', 400, 400)

# register event handlers for control elements and start frame
b1 = frame.add_button('Range is [0, 100)', range100, 200)
b2 = frame.add_button('Range is [0, 1000)', range1000, 200)
frame.add_input('Guess', input_guess, 200)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
