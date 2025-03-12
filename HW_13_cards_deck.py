import random


class Card:
    number_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    mast_list = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self, number, mast):
        self.number = number
        self.mast = mast

    def __str__(self):
        return f'{self.number} {self.mast}'


class CardsDeck:
    def __init__(self):
        self.cards_deck = []
        self.create_deck()

    def create_deck(self):
        for i in Card.number_list:
            for j in Card.mast_list:
                self.cards_deck.append(Card(i, j))
        self.cards_deck.append('Joker Red')
        self.cards_deck.append('Joker Black')

    def get(self, card_num):
        return self.cards_deck[card_num - 1]

    def shuffle(self):
        return random.shuffle(self.cards_deck)


cd = CardsDeck()

cd.shuffle()

card_number = int(input('Choose the card from 54 cards deck '))
card = cd.get(card_number)
print(f'Your card is: {card}')

cd.shuffle()

card_number = int(input('Choose the card from 54 cards deck '))
card = cd.get(card_number)
print(f'Your card is: {card}')
