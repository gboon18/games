#!/usr/bin/env python

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank = rank, suit = suit))
    
    def __str__(self):   
        card_str = ''     
        for card in self.deck:
            card_str += '\n' + card.__str__()
        return 'The deck has:'+card_str

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop(0)

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def __str__(self):
        # print(self.value)
        output = 'Cards in Hand are:'
        for card in self.cards:
            output += '\n'+card.__str__()
        output += f'\nAnd the total value is: {self.value}' 
        return output

    def add_card(self,card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == "Ace":
            self.aces += 1
        self.adjust_for_ace()

    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def __str__(self):
        return f"You have {self.total} and you bet {self.bet}."
    
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    
    # ask for the bet
    # check if can take the bet
    while True:
        try:
            chips.bet = int(input('What is your bet? '))
        except ValueError:
            print("\nIt's gotta be an integer.")
        else:
            if chips.bet > chips.total:
                print(f"\nYou only have {chips.total}. Bet a smaller or an equal amount to what you have.")
            else:
                print(f"\nYou are betting {chips.bet} out of your total, {chips.total}. Good luck.")
                break

def hit(deck,hand):
    
    hand.add_card(deck.deal())

def hit_or_stand(deck,hand):
    global playing # to control an upcoming while loop
    
    while True:
        h_or_s = input('Hit (h) or Stand (s)?')
        if h_or_s.lower() == 'h':
            print('The player hits.')
            hit(deck, hand)
        elif h_or_s.lower() == 's':
            print('The player stands.')
            playing = False
        else:
            print('Wrong input. Try again.')
            continue
        break

def show_some(player,dealer):
    print("\nDealer's hand: ")
    print("<card hidden>")
    print(dealer.cards[1])
    print("\nPlayer's Hand:")
    print(*player.cards, sep='\n')

def show_all(player,dealer):
    print("\nDealer's Hand:")
    print(*dealer.cards, sep='\n')
    print("The dealer's total value is ", dealer.value)
    print("\nPlayer's Hand:")
    print(*player.cards, sep='\n')
    print("The player's total value is ", player.value)

def player_busts(chips):
    print('\nPlayer busts!\n')
    chips.lose_bet()

def player_wins(chips):
    print('\nPlayer wins!\n')
    chips.win_bet()

def dealer_busts(chips):
    print('\nDealer busts!\n')
    chips.win_bet()
    
def dealer_wins(chips):
    print('\nDealer wins!\n')
    chips.lose_bet()
    
def push():
    print("\nIt's a push!\n")

stateofplay = True
# Set up the Player's chips
player_chips = Chips()
while stateofplay:
    # Print an opening statement
    print("\nLet's start the game. You know the rule, right? Good.\n")

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    print("Deck created and shuffled.")
    dealer = Hand()
    player = Hand()
    hit(deck, player)
    hit(deck, dealer)
    hit(deck, player)
    hit(deck, dealer)
    print("Two cards dealed each to the player and the dealer.")
    
    print("\nThe player chips value is: ", player_chips.total)    
    
    # Prompt the Player for their bet
    print('\nPlayer, ')
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player, dealer)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player, dealer)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value > 21:
            player_busts(player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player.value <= 21:
        while dealer.value <= 17:
            hit(deck, dealer)
    
        # Show all cards
        show_all(player, dealer)
    
        # Run different winning scenarios
        if dealer.value > 21:
            dealer_busts(player_chips)
        elif dealer.value > player.value:
            dealer_wins(player_chips)
        elif dealer.value < player.value:
            player_wins(player_chips)
        else:
            push()

    
    # Inform Player of their chips total 
    print(f"Now you have {player_chips.total}")
    
    # Ask to play again
    while True:
        yorn = input("\nDo you want to play again? [y/n]\n")
        if yorn.lower() == 'y' and player_chips.total > 0:
            print("\nAlright! Let's play one more time!")
            stateofplay = True
            playing=True
            break
        elif yorn.lower() == 'n' and player_chips.total > 0:
            print("\nGood game. Come again!")
            stateofplay = False
            break
        elif player_chips.total == 0:
            print("\nWait wait wait! You have no money left. GTFO of our casino perimeter!\n")
            stateofplay = False
            break
        else:
            print("\nWrong input. Try again. It's y or n answer.\n")
        