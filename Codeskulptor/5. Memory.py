import simplegui
import random

cards = []
exposed = [False for i in range(16)]
state = 0
card_size = [50,100]
turns = 0
last_card = [0 for i in range(3)]

numbers = range(8)
numbers.extend(numbers)

def new_game():
    global numbers, state, exposed, last_card, turns
    random.shuffle(numbers)
    state = 0
    exposed = [False for i in range(16)]
    last_card = [0 for i in range(3)]
    turns = 0
    label.set_text("Turns: " + str(turns))
    
def set_state():
    global state
    if state == 0:
        state = 1
    elif state == 1:
        state = 2
    else:
        state = 1

def click(pos):
    global turns
    if exposed[pos[0] // card_size[0]] == False:
        exposed[pos[0] // card_size[0]] = True
        if state == 2:
            turns += 1
            
    if turns == 0:
        last_card[state] = pos[0] // card_size[0]
    else: 
        last_card[0] = last_card[2]
        last_card[state] = pos[0] // card_size[0]
    
    if state == 2:
        if numbers[last_card[0]] != numbers[last_card[1]]:
            exposed[last_card[0]] = False
            exposed[last_card[1]] = False
    set_state()
    label.set_text("Turns: " + str(turns))
    
                     
def draw(canvas):
    if exposed != []:
        for i in range(len(exposed)):
            if exposed[i]:
                canvas.draw_text(str(numbers[i]), [(2 * i + 1) * card_size[0] / 2 - 10, card_size[1] * 2 / 3], 48, 'white')
            else:
                canvas.draw_polygon([[i * card_size[0], 0], [(i + 1) * card_size[0], 0], [(i+1) * card_size[0], card_size[1]],[i * card_size[0], card_size[1]]], 1, 'white', 'green')
    
f = simplegui.create_frame('Memory', card_size[0] * 16, card_size[1])
f.add_button('Restart', new_game, 100)

f.set_draw_handler(draw)
f.set_mouseclick_handler(click)
label = f.add_label("Turns: 0")
    
new_game()
f.start()
