import simplegui
import math
import random

range = 100 
n = 0
count = 0
number = 0
newgame = ''
message = ''
result = ''

def new_game():
    global count, newgame
    count = 0
    global number
    number = random.randrange(0, range)
    global n 
    n = math.ceil(math.log2(range))
    
    newgame = f"New game. Range is from 0 to {range}. Number of remaining guesses is {n-count}"



def range1000():
    global range
    range = 1000 
    return new_game()


def range100():
    global range 
    range = 100 
    return new_game()

def input_guess(guess):
    global message, result
    guess = int(guess)
    
    global count
    count += 1
    
    message = f"Guess was {guess}. Number of remaining guesses is {n - count}"
    
    if count < n:
        if number == guess:
            result = "Correct"
            new_game()
        elif number > guess:
            result = "Higher"
        else:
            result = "Lower"
    else: 
        result = f"Ran out of guesses. The secret number was {number}"
        new_game()
        
        
def draw(canvas):
    canvas.draw_text(newgame, [50,80], 18, 'white')
    canvas.draw_text(message, [50, 100], 18, 'white')
    canvas.draw_text(result, [50, 120], 18, 'yellow')

f = simplegui.create_frame("guess the number", 600, 200)

f.add_button("Range is 100", range100, 200)
f.add_button("Range is 1000", range1000, 200)
f.add_input("Enter a guess", input_guess, 100)
f.set_draw_handler(draw)

new_game()
f.start()
