import random as rand

suites = ["Hearts", "Diamonds", "Spades", "Clubs"]
numbers = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
deck = []
shuffledDeck = []

# initiate cards and deck
for i in range(0, 4):
    for x in range(0, 13):
        deck.append(numbers[x] + " of " + suites[i])

# shuffle the deck
for i in deck:
    shuffledDeck.insert(int(rand.random()*len(shuffledDeck)), i)

print(shuffledDeck)
