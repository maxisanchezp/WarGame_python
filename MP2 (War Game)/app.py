##CARD
##SUIT, RANK, VALUE
##import random

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two','Three','Four','Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = { "Two":2, 'Three': 3, 'Four': 4, 'Five': 5,"Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
          'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit
    


class Deck:
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                ##CREATE THE CARD OBJECT
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)   
        
    def deal_one(self):
        return self.all_cards.pop()
    
          

# len(new_deck.all_cards)
# print(mycard)
# lc = new_deck.all_cards[0]

# print(lc)

class Player:
    
    def __init__(self, name):
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            ##LIST OF MULTIPLE CARD OBJECTS
            self.all_cards.extend(new_cards)
        else:
            ##SINGLE CARD OBJECT
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'
    

#print(mycard)


#GAME SETUP
player1 = Player("One")
player2 = Player("Two")


new_deck = Deck()
new_deck.shuffle()


for x in range(26):
    player1.add_cards(new_deck.deal_one())
    player2.add_cards(new_deck.deal_one())
    

game_on = True

round_number = 0

while game_on:
    round_number += 1
    print(f'Currently on round {round_number}')
    
    if len(player1.all_cards) == 0:
        print('Player 1 out of cards, Player 2 wins!')
        game_on = False
        break
    
    
    if len(player2.all_cards) == 0:
        print('Player 2 out of cards, Player 1 wins!')
        game_on = False
        break
    
    #START A NEW ROUND
    player1_cards = []
    player1_cards.append(player1.remove_one())
    
    player2_cards = []
    player2_cards.append(player2.remove_one())
    
            
    at_war = True
    #WHILE AT WAR
    while at_war:
        if player1_cards[-1].value > player2_cards[-1].value:
            player1.add_cards(player1_cards)
            player1.add_cards(player2_cards)
            
            at_war = False
            
        elif player2_cards[-1].value > player1_cards[-1].value:
            player2.add_cards(player1_cards)
            player2.add_cards(player2_cards)
            
            at_war = False
            
        else:
            print('WAR!')
            if len(player1.all_cards) < 5:
                print('Player 1 unable to declare war')
                print('Player 2 WINS')
                game_on = False
                break
            
            elif len(player2.all_cards) < 5:
                print('Player 2 unable to declare war')
                print('Player 1 WINS')
                game_on = False
                break
            
            else:
                for num in range(5):
                    player1_cards.append(player1.remove_one())
                    player2_cards.append(player2.remove_one())