# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 900
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_pos = [WIDTH / 2, HEIGHT / 2]
LEFT = False
RIGHT = True
direction = RIGHT
INC = 1.10 # to increase ball speed when it hits the paddles

# initialize BALL and PADDLES
def spawn_ball(direction):
    global ball_pos, ball_vel
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == RIGHT :
        ball_vel = [random.randrange(5, 10), - (random.randrange(3, 6))]
    elif direction == LEFT :
        ball_vel = [ - (random.randrange(5, 10)), - (random.randrange(3, 6))]


# Event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  
    global score1, score2, hard  
    spawn_ball(direction)
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2 
    paddle1_vel, paddle2_vel = 0, 0
    score1 = 0
    score2 = 0
    hard = False # to set the game to hard
    
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
    global INC, hard
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] +=  ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1] >= HEIGHT - BALL_RADIUS :
        ball_vel[1] = -(ball_vel[1])
    elif ball_pos[1] <= BALL_RADIUS :
        ball_vel[1] = -(ball_vel[1])
  
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 20, "White", 'White')
    
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos + paddle1_vel >= HALF_PAD_HEIGHT) and (paddle1_pos + paddle1_vel + HALF_PAD_HEIGHT <= HEIGHT) :
        paddle1_pos += paddle1_vel
    if (paddle2_pos + paddle2_vel >= HALF_PAD_HEIGHT) and (paddle2_pos + paddle2_vel + HALF_PAD_HEIGHT <= HEIGHT) :
        paddle2_pos += paddle2_vel
     
    # draw paddles
    canvas.draw_line([0, paddle1_pos - HALF_PAD_HEIGHT], [0, paddle1_pos + HALF_PAD_HEIGHT], 2 * PAD_WIDTH, "White")
    canvas.draw_line([WIDTH, paddle2_pos - HALF_PAD_HEIGHT], [WIDTH, paddle2_pos + HALF_PAD_HEIGHT], 2 * PAD_WIDTH, "White")
 
    # determine whether paddle and ball collide 
    if ball_pos[0] + BALL_RADIUS > (WIDTH - PAD_WIDTH) :
        if (ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT) and ball_pos[1] <= (paddle2_pos + HALF_PAD_HEIGHT) :  
            ball_vel[0] = - (ball_vel[0] * INC) #Increments ball_vel
        else:
            score1 += 1
            spawn_ball(LEFT)
    elif ball_pos[0] - BALL_RADIUS < PAD_WIDTH : 
        if (ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT) and (ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT) :
            ball_vel[0] = - (ball_vel[0] * INC) # Increments ball_vel
        else:
            score2 += 1
            spawn_ball(RIGHT)
    
    # draw scores
    str_score1 = str(score1)
    str_score2 = str(score2)
    canvas.draw_text(str_score1, [WIDTH / 4, HEIGHT / 8], 48, "Red")
    canvas.draw_text(str_score2, [WIDTH * 3 / 4, HEIGHT / 8], 48, "Red")
    
    #set the game HARD - >:]]
    if hard == True : 
        canvas.draw_text('Game is now HARD!', [15, HEIGHT], 20, "Red")

        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"] :
        paddle1_vel = - 10
    elif key == simplegui.KEY_MAP["s"] :
        paddle1_vel = 10
    if key == simplegui.KEY_MAP['up'] :
        paddle2_vel = - 10
    elif key == simplegui.KEY_MAP['down'] :
        paddle2_vel = 10
                
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = 0
    paddle2_vel = 0

def restart():
    new_game()

def hard():
    global INC, hard
    INC = 1.2
    hard = True
    

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', restart, 200)
frame.add_button('HARD', hard, 200)



# start frame
new_game()
frame.start()
