import random


def name_to_number(name):
    if name == 'rock' : return 0
    elif name == 'Spock' : return 1
    elif name == 'paper': return 2
    elif name == 'lizard': return 3
    elif name == 'scissors' : return 4
    else:
        print('NOT A VALID NAME')
    
def number_to_name(number):
    if number == 0 : return 'rock'
    if number == 1 : return 'Spock'
    if number == 2 : return 'paper'
    if number == 3 : return 'lizard'
    if number == 4 : return 'scissors'
    else:
        print('NOT A VALID NUMBER')

def rpsls(player_choice): 
    
    # print a blank line to separate consecutive games
    print('\n')
    
    # print out the message for the player's choice
    print('Player chooses ' + player_choice)
    
    # convert the player's choice to player_number using the function name_to_number()
    name = player_choice
    player_choice = name_to_number(name)
    
    # compute random guess for comp_number using random.randrange()
    comp = random.randrange(0,5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice =  number_to_name(comp)
    
    # print out the message for computer's choice
    print('Computer chooses '+comp_choice)
    
    # compute difference of comp_number and player_number modulo five
    win = (comp - player_choice) % 5
    
    # use if/elif/else to determine winner, print winner message
    if win > 2 : print('**Player Wins**')
    elif 0 < win < 3  : print('**Computer Wins**')
    elif win == 0 : print('Player and computer tie!')
    else: print('Wait...something wicked happened')
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


