# template for "Stopwatch: The Game"

import simplegui

# define global variables
t = 0
result = '0:00.0'

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global result
    A = t // 600 
    B = ((t // 10) % 60 ) // 10
    C = ((t // 10) % 60 ) % 10
    D =  (t % 10 ) % 10
    result = str(A) + ":" + str(B) + str(C) + "." + str(D)
    

    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    timer.stop()
    
def reset():
    global t
    timer.stop()
    t = 0
    format(t)
    
    
# define event handler for timer with 0.1 sec interval
def tenth_seconds():
    global t
    t += 1
    format(t)

# define draw handler
def draw(canvas):
    global t
    canvas.draw_text(result, [40,75], 35, "White")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 150, 150)

# register event handlers
timer = simplegui.create_timer(100, tenth_seconds)
frame.set_draw_handler(draw)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

# start frame
frame.start()


# Please remember to review the grading rubric
