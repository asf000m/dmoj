# DMOJ coci17c1p1
# COCI '17 Contest 1 #1 Cezar


# INPUT
num_cards_drawn = int(input())

cards_drawn = []
for _ in range(num_cards_drawn):
    card = int(input())
    cards_drawn.append(card)

# create a deck of 52 cards
deck = []

# ranks 2 through 9 and 11 (Ace) for each 4 suits
for rank in [2, 3, 4, 5, 6, 7, 8, 9, 11]:
    # create a card for each suit
    for suit in range(4):
        deck.append(rank)

# ranks of value 10 (10, Jack, Queen, King) for each 4 suits
for rank in range(16):
    deck.append(10)

# remove the cards drawn from the deck
for card in cards_drawn:
    deck.remove(card)

sum_cards_drawn = sum(cards_drawn)

# x is the difference from the sum of the cards so far to 21
x = 21 - sum_cards_drawn

# verify the number of remaining cards in the deck
cards_greater_x = 0
cards_less_equal_x = 0
for card in deck:
    if card > x:
        cards_greater_x += 1
    else:
        cards_less_equal_x += 1

# OUTPUT
if cards_greater_x >= cards_less_equal_x:
    print("DOSTA")
else:
    print("VUCI")
