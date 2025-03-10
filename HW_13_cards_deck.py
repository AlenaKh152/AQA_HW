import random


class Card:
    number_list = ['2' ,'3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    mast_list = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    card_list = []

    def __init__(self):
        for i in self.number_list:
            for j in self.mast_list:
                self.card_list.append(i + ' ' + j)
        self.card_list.append('Joker Red')
        self.card_list.append('Joker Black')


class CardsDeck(Card):
    def __init__(self):
        super().__init__()

    def get(self, card_num):
        return self.card_list[card_num - 1]

    def shuffle(self):
        return random.shuffle(self.card_list)


cd = CardsDeck()
cd.shuffle()

card_number = int(input('Choose the card from 54 cards deck '))
card = cd.get(card_number)
print(f'Your card is: {card}')

cd.shuffle()

card_number = int(input('Choose the card from 54 cards deck '))
card = cd.get(card_number)
print(f'Your card is: {card}')
