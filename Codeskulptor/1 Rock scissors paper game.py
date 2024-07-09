# import libs
import simplegui
import random

result = ''
message = ''
error = ''

choice_dict = {"rock":0, "Spock":1, "paper":2, "lizard":3, "scissors":4}
choice_dict_reverse = {value:key for key, value in choice_dict.items()}

def choice(text):
    global message, error
    if text in choice_dict.keys():
        player_num = choice_dict[text]
        comp_num = random.randrange(0,5)
        comp = choice_dict_reverse[comp_num]

        message = f"Player chose {text} and Computer chose {comp}"

        global result
        diff = (player_num - comp_num) % 5
        if diff >= 3: 
            result = "Computer wins!"
        elif diff >= 1:
            result = "Player wins!"
        else: 
            result = "Player and Computer tie"
    else: error = "Typo. Re-enter your choice."

def draw(canvas):
    canvas.draw_text(message, [50, 90], 24, 'white')
    canvas.draw_text(result, [50, 110], 24, 'yellow')
    canvas.draw_text(error, [50, 90], 24, 'red')
        
# create a gui frame
frame = simplegui.create_frame("rspls game", 600, 200)
frame.add_input("Enter your choice", choice, 100)
frame.set_draw_handler(draw)

frame.start()
    
    