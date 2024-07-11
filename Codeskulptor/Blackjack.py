import simplegui
import random

card_sz = (72, 96)
card_ct = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

card_b_sz = (72, 96)
card_b_ct = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png") 

in_play = False
outcome = ""
score = 0
message = ''

suits = ('C', 'S', 'H', 'D')
ranks = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
values = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.suit + self.rank
    
    def get_suit(self):
        return self.suit
    
    def get_rank(self):
        return self.rank
    
    def draw(self, canvas, pos):
        loc = [ranks.index(self.rank) * card_sz[0] + card_ct[0], suits.index(self.suit) * card_sz[1] + card_ct[1]]
        canvas.draw_image(card_images, loc, card_sz, [pos[0] + card_ct[0], pos[1] + card_ct[1]], card_sz)

class Hand:
    def __init__(self):
        self.cards = []
    
    def __str__(self):
        return self.cards
    
    def add_card(self, card): # card is a Card object
        self.cards.append(card)
    
    def get_value(self):
        hand_value = 0
        for card in self.cards: 
            if card.get_rank() != 'A':
                hand_value += values[card.get_rank()]
            else:
                if hand_value + 10 <= 21:
                    hand_value += values[card.get_rank()]
                    hand_value += 10
        return hand_value
    
    def draw(self, canvas, pos):
        canvas.draw_image(card_back, [card_b_ct[0], card_b_ct[1]], card_b_sz, [pos[0] + card_ct[0], pos[1] + card_ct[1]], card_b_sz)
        
    
class Deck:
    def __init__(self):
        self.cards = [i+j for i in suits for j in ranks]
        
    def deal(self, card): # card is a Card object
        card_name = card.get_suit() + card.get_rank()
        self.cards.remove(card_name)
    
    def shuffle(self):
        random.shuffle(self.cards)
        
# objects
deck = Deck()
dealer_hand = Hand()
player_hand = Hand()
        
# define handlers for buttons
def deal():
    global deck, dealer_hand, player_hand, in_play, outcome, score

    deck = Deck()
    deck.shuffle()
    
    dealer_hand.cards = []
    player_hand.cards = []
    
    for i in range(2):
        card = random.choice(deck.cards)
        card = Card(card[0], card[1])

        dealer_hand.add_card(card)
        deck.deal(card)
    
        
    for i in range(2):
        card = random.choice(deck.cards)
        card = Card(card[0], card[1])

        player_hand.add_card(card)
        deck.deal(card)
        
    outcome = 'Hit or stand?'
    
    if in_play:
        score -= 1
        outcome = 'Punish 1 score. Sorry!'
        
    in_play = True

def hit():
    global outcome
    card = random.choice(deck.cards)
    card = Card(card[0], card[1])
    player_hand.add_card(card)
    deck.deal(card)
    
    outcome = 'Hit or stand?'
    
def stand():
    global score, in_play, outcome, message

    while dealer_hand.get_value() < 17:
        card = random.choice(deck.cards)
        card = Card(card[0], card[1])

        dealer_hand.add_card(card)
        deck.deal(card)
    
    in_play = False
    if dealer_hand.get_value() > 21 and player_hand.get_value() > 21:
        score += 0
        message = 'Push'
    if dealer_hand.get_value() > 21:
        score += 1
        message = 'You win'
    elif player_hand.get_value() > 21:
        score -= 1
        message = 'You lose'
    elif dealer_hand.get_value() >= player_hand.get_value():
        score -= 1
        message = 'You lose'
    elif dealer_hand.get_value() < player_hand.get_value():
        score += 1
        message = 'You win'
           
        
    outcome = 'New deal?'
             
        
        
def draw(canvas):
    if dealer_hand.cards != []:
        if in_play:
            for i in range(len(dealer_hand.cards)):
                pos = [i * card_sz[0] + 50, 200]
                dealer_hand.cards[i].draw(canvas, pos)
            dealer_hand.draw(canvas, [50, 200])
        else:
            for i in range(len(dealer_hand.cards)):
                pos = [i * card_sz[0] + 50, 200]
                dealer_hand.cards[i].draw(canvas, pos)

        for i in range(len(player_hand.cards)):
            pos = [i * card_sz[0] + 50, 400]
            player_hand.cards[i].draw(canvas, pos)
    
    canvas.draw_text(f"Your score = {score}", [420,100], 24, 'yellow')
    canvas.draw_text(message, [420, 80], 24, 'yellow')
    canvas.draw_text('BLACKJACK', [50, 100], 48, 'white')
    canvas.draw_text('Dealer hand', [50, 150], 24, 'green')
    canvas.draw_text('Your hand', [50, 350], 24, 'green')
    canvas.draw_text(outcome, [200, 350], 24, 'yellow')
    
f = simplegui.create_frame('Blackjack', 600, 600)
f.add_button('Deal', deal, 100)
f.add_button('Hit', hit, 100)
f.add_button('Stand', stand, 100)
f.set_draw_handler(draw)

f.start()
deal()