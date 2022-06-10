import simplegui

# global variables
WIDTH = 300
HEIGHT = 200
time = 0
str_time = str(time)
success = 0
total = 0


def format(t):
    ''' Transforms time into a 5-len string '''
    global time, str_time
    time = t
    str_time = str(t)
    if (time > 999) and (time < 10000) :
        return str(int(str_time[:2]) // 6) + ':' + str(int(str_time[0:2]) % 6) + str_time[2] + '.' + str_time[3]
    elif (time > 599) and (time < 1000) :
        return str(int(str_time[0]) // 6) + ':' + str(int(str_time[0]) % 6) + str_time[1] + '.' + str_time[2]
    elif (time > 99) and (time < 600) : 
        return '0:'+ str(int(str_time[0]) % 6) + str_time[1] + '.' + str_time[2]
    elif (time > 9) and (time < 100) : 
        return '0:0' + str_time[0] + '.' + str_time[1]
    elif (time > 0) and (time < 10) : 
        return '0:00.' + str_time[0]
    elif time == 0 : return '0:00.0'

def game():
    ''' Handler to update the game '''
    global success, total
    return str(success) + '/' + str(total)

def start():
    global stop
    timer.start()
    stop = True
    
def stop():
    global success, total, time, stop, x
    timer.stop()
    if (stop == True) and (format(time)[5] == '0') :
        success += 1
        total += 1
    elif stop == True :
        total += 1
    stop = False

def reset():
    global time, total, success
    time = 0
    success = 0
    total = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global time 
    time += 1

# Draw handler
def draw(canvas):
    canvas.draw_text(format(time), [(WIDTH / 2 - 30), (HEIGHT / 2)], 30, "Red")
    canvas.draw_text(game(), [(WIDTH - 30), (HEIGHT - 180)], 20, "White")   

# Frame
frame = simplegui.create_frame('STOP and WATCH', WIDTH, HEIGHT)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)

# register event handlers
start = frame.add_button('START', start, 75)
stop = frame.add_button('STOP', stop, 75)
reset = frame.add_button('RESET', reset, 75)

# start frame
frame.start()

