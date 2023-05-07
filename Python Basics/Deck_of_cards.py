from __future__ import annotations
from dataclasses import dataclass
from random import shuffle


class Deck:
    CARD_COLORS = ["♥", "♦", "♠", "♣"]
    CARD_SYMBOLS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self) -> None:
        self.last_dealt_card = None
        self.deck = [Card(symbol, color)
                     for symbol in Deck.CARD_SYMBOLS
                     for color in Deck.CARD_COLORS]

    def __str__(self) -> str:
        return ", ".join([str(card) for card in self.deck])

    def shuffle(self) -> None:
        shuffle(self.deck)

    def deal_card(self) -> None:
        try:
            self.last_dealt_card = self.deck[-1]
            self.deck.pop(-1)
        except IndexError:
            print("No more cards to deal")

    def show_dealt_card(self) -> None:
        print(self.last_dealt_card)


@dataclass
class Card:
    symbol: str
    color: str

    def __str__(self) -> str:
        return f'{self.symbol}{self.color}'


def main():
    deck = Deck()
    deck.shuffle()
    deck.deal_card()
    deck.show_dealt_card()
    for i in range(60):
        deck.deal_card()
        deck.deal_card()
        deck.show_dealt_card()


if __name__ == '__main__':
    main()
