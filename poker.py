# -*- coding: UTF-8 -*-

# writen by leon
#writen time :2019/10/19

import random
import codecs
import copy
#-------------------------------------------------------------------------------
#phase 1:  make a new deck of playing cardJokers
#-------------------------------------------------------------------------------
# initialize
cardJokers=('Red Joker','Black Joker')
cardMarks=('♠','♥','♦','♣')
cardNumbers=('2','3','4','5','6','7','8','9','10','J','Q','K','A')


# make a deck of playing card
deck=[]

#add jokers first

for c in cardJokers:
    deck.append(c)

#add 4*13 cards
for cn in cardNumbers:
    for cm in cardMarks:
        card=cm+cn
        deck.append(card)

print(len(deck))
print(deck)


#stard shuffle
print('-------===========<<<([{  cutting line  }])>>>============-------')
shuffled_deck=[]

'''
for times in range(0,len(deck)):
    picked_card = random.choice(deck)
    shuffled_deck.append(picked_card)
    deck.remove(picked_card)
'''


#method-2 of shuffled

shuffled_deck=copy.copy(deck)
random.shuffle(shuffled_deck)


print(deck)



#record a new deck to a text file
file_name="deck-new-54.txt"
f=codecs. open(file_name, 'w','utf-8')

for card in shuffled_deck:
    f.write(card)
    f.write('\n')
f.close()


#start the deal
print('-------===========<<<([{  cutting line  }])>>>============-------')
num_of_players = 3
card_of_player=int(len(shuffled_deck)/num_of_players)
print('We have %d players, every one has %d cards.'
    %(num_of_players,card_of_player))



player1_deck=[]
player2_deck=[]
player3_deck=[]



for times in range(card_of_player):
    picked_card = random.choice(shuffled_deck)
    player1_deck.append(picked_card)
    shuffled_deck.remove(picked_card)

    picked_card = random.choice(shuffled_deck)
    player2_deck.append(picked_card)
    shuffled_deck.remove(picked_card)

    picked_card = random.choice(shuffled_deck)
    player3_deck.append(picked_card)
    shuffled_deck.remove(picked_card)

print('\nPlayer 1-cards is :')
print(player1_deck)
print('\nPlayer 2-cards is :')
print(player2_deck)
print('\nPlayer 3-cards is :')
print(player3_deck)
