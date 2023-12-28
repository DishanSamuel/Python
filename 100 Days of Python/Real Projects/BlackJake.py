import random 

cards = [11 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,10 ,10 ,10 ]

player_cards = []
computer_cards = []


for i in range(0,2):

    player_cards += [random.choice(cards)]
    computer_cards += [random.choice(cards)]

