#!/usr/bin/env python3

import random


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def get_name(self):
        return self.name

    def add_card_to_hand(self, card):
        if card != None:
            self.hand.append(card)

    def remove_card_from_hand(self, card):
        self.hand.remove(card)

    def hand_size(self):
        return len(self.hand)


class CardDeck(object):
    """A deck of cards 2-9 od spades, hearts, diamonds, clubs"""

    def __init__(self):
        hearts = "2H,3H,4H,5H,6H,7H,8H,9H"
        spades = "2S,3S,4S,5S,6S,7S,8S,9S"
        diamonds = "2D,3D,4D,5D,6D,7D,8D,9D"
        clubs = "2C,3C,4C,5C,6C,7C,8C,9C"
        self.deck = (
            hearts.split(",")
            + spades.split(",")
            + diamonds.split(",")
            + clubs.split(",")
        )

    def get_card(self):
        """Returns a random card, or None of none are left"""
        if len(self.deck) < 1:
            return None
        else:
            card = random.choice(self.deck)
            self.deck.remove(card)
            return card

    def compare_cards(self, card1, card2):
        """returns the larger card according to
        (1) the larger of the numbers, or if equal
        (2) spades > hearts > diamonds > clubs
        """
        if card1[0] > card2[0]:
            return card1
        elif card1[0] < card2[0]:
            return card2
        elif card1[1] > card2[1]:
            return card1
        else:
            return card2

    def print_deck(self):
        return self.deck


name1 = input("What is the name of player 1? ")
player1 = Player(name1)

name2 = input("What is the name of player 2? ")
player2 = Player(name2)

deck = CardDeck()

while True:
    player1_card = deck.get_card()
    player2_card = deck.get_card()
    player1.add_card_to_hand(player1_card)
    player2.add_card_to_hand(player2_card)

    if player1_card == None or player2_card == None:
        print("Game over.  No more cards in deck.")
        print(name1, " has ", player1.hand_size())
        print(name2, " has ", player2.hand_size())
        print("Who won?")
        if player1.hand_size() > player2.hand_size():
            print(name2, " wins!")
        elif player1.hand_size() < player2.hand_size():
            print(name1, " wins!")
        else:
            print("A tie!")
        break
    else:
        print(name1, ": ", player1_card)
        print(name2, ": ", player2_card)
        if deck.compare_cards(player1_card, player2_card) == player1_card:
            player2.add_card_to_hand(player1_card)
            player1.remove_card_from_hand(player1_card)
        else:
            player1.add_card_to_hand(player2_card)
            player2.remove_card_from_hand(player2_card)
