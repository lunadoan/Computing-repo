import simplegui

ticks = 0
count_stop = 0
count_stop_whole = 0
    
def tick():
    global ticks
    ticks += 1
    
def format_time(ticks):
    minute = ticks // 600
    second = (ticks / 10) % 60
    
    if second < 10:
        return f"{minute}:0{second:.1f}"
    else:
        return f"{minute}:{second:.1f}"
    
def draw(canvas):
    canvas.draw_text(format_time(ticks), [70,120], 30, 'white')
    
    # check if stopwatch stops at round second
    canvas.draw_text(f"{count_stop_whole}/{count_stop}", [95,25], 20, 'red')

def stop():
    timer.stop()
    global count_stop, count_stop_whole, ticks
    count_stop += 1
    
    if ticks % 10 == 0:
        count_stop_whole += 1
    
def start():
    timer.start()
    
def reset():
    global ticks, count_stop, count_stop_whole
    ticks = 0
    count_stop = 0
    count_stop_whole = 0
    
frame = simplegui.create_frame("stopwatch", 200, 200)
timer = simplegui.create_timer(100, tick)

frame.add_button('start', start, 150)
frame.add_button('stop', stop, 150)
frame.add_button('reset', reset, 150)

frame.set_draw_handler(draw)

frame.start()
timer.start()
                               