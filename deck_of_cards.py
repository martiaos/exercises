import numpy as np

suits = ['C', 'S', 'D', 'H']
numbers = [i for i in range(1,14)]
cards = []

for i in suits: #for each suit
    for n in numbers: #for each number
        cards.append((n,i)) #add entry to deck

np.random.shuffle(cards) #randomize list

drawn = cards[0:13]

sorted = [] #finished list

for type in suits: #for each suit
    table = [] #workspace for sorting
    for card in drawn: #draw all cards
        if card[1] == type: #if suit matches
            table.append(card) #add it to table
    table.sort() #sort the table
    sorted.append(table) #add sorted table to finished list

print(sorted) #return sorted list
