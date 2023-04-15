import random

class Deck:
    card_colors = ["♥", "♦", "♠", "♣"]
    card_symbols = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self):
        # Initialize deck of 52 unique cards
        self.deck = [Card(symbol, color) for symbol in Deck.card_symbols
                     for color in Deck.card_colors]

    def __repr__(self):
        return ", ".join([card.__str__() for card in self.deck])

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        # Draw last card form the deck, print card to the user and remove from deck
        try:
            card = self.deck[-1]
            self.deck.pop(-1)
        except IndexError:
            print("No more cards to deal")
        else:
            print(f'Dealt card: {card}')

class Card:
    def __init__(self, symbol, color):
        self.symbol = symbol
        self.color = color

    def __repr__(self):
        return f'{self.symbol}{self.color}'


def main():
    deck = Deck()

    # Class methods test
    print(deck)
    deck.shuffle()
    deck.deal()
    print(deck)
    deck.deal()


if __name__ == '__main__':
    main()
