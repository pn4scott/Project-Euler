import simplegui
import random

#initialize globals
BALL_RADIUS = 5
WIDTH = 400
HEIGHT = 500
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [3, -2]
PAD_WIDTH = 70
PAD_HEIGHT = 8
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
pad_pos = [WIDTH / 2, HEIGHT - (PAD_HEIGHT/2)]
pad_vel = 0

#define event handlers
def new_game():
    global pad_pos, pad_vel, score, score_string, ball_vel, ball_pos
    score_string = "0"
    score = 0
    pad_pos = [WIDTH / 2, HEIGHT - (PAD_HEIGHT/2)]
    pad_vel = 0
    ball_pos = [WIDTH / 2, HEIGHT / 2] 
    ball_vel = [random.randrange(1,2), random.randrange(-2,-1)]
    
def restart():
    new_game()
    
def stop():
    global score, ball_pos, ball_vel
    ball_vel = [0,0]

#keeps the paddle on screen
def limit():
    global pad_pos, pad_vel
    
    if pad_pos[0] < HALF_PAD_WIDTH:
        pad_pos[0] = HALF_PAD_WIDTH
        pad_vel = 0
        
    elif pad_pos[0] > WIDTH - HALF_PAD_WIDTH:
        pad_pos[0] = WIDTH - HALF_PAD_WIDTH
        pad_vel = 0
        
        
def draw(canvas):
    global pad_pos, pad_vel, pad_left, pad_right, score, score_string
    
    #update ball position
    limit()
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    #update paddle's horizontal position
    pad_pos[0] += pad_vel
    
    #reflecting off top wall
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    
    #reflecting off the right wall
    if ball_pos[0] >= (WIDTH - BALL_RADIUS):
        ball_vel[0] = -ball_vel[0]
    
    #reflecting off the left wall 
    if ball_pos[0] <= BALL_RADIUS:
        ball_vel[0] = -ball_vel[0]
        
    #draw paddle
    pad_left = [pad_pos[0] - HALF_PAD_WIDTH, pad_pos[1]]
    pad_right = [pad_pos[0] + HALF_PAD_WIDTH, pad_pos[1]]
    canvas.draw_line(pad_left, pad_right, PAD_HEIGHT, "White")
        
    #collision with gutter/bottom of canvas
    if ball_pos[1] >= HEIGHT - PAD_HEIGHT - BALL_RADIUS:
        if (pad_left[0] <= ball_pos[0] <= pad_right[0]):
            ball_vel[1] = -ball_vel[1] * 1.2
            score += 1
            score_string = str(score)
        else:
            new_game()
    
    #draw ball and scores
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "Red")
    canvas.draw_text(score_string, (370, 50), 30, "White")
    
    #draw bottom gutter
    canvas.draw_line([0, (HEIGHT - PAD_HEIGHT)], [WIDTH, (HEIGHT - PAD_HEIGHT)], 1, "White")
     

#right and left arrow keys
def keydown(key):
    acc = 3
    global pad_vel
    
    if key == simplegui.KEY_MAP["left"]:
        pad_vel -= acc
        
    if key == simplegui.KEY_MAP["right"]:
        pad_vel += acc
        
            
def keyup(key):
    global pad_vel
    
    if key == simplegui.KEY_MAP["left"]:
        pad_vel = 0
    if key == simplegui.KEY_MAP["right"]:
        pad_vel = 0
    
#create frame
frame = simplegui.create_frame("Project 1", WIDTH, HEIGHT)

#register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restart, 100)
frame.add_button("Stop", stop, 100)

#start frame
frame.start()
new_game()