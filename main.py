# Blackjack Project

import random
from os import system
from art import logo

# clears console and print game logo
def clear():
  _ = system('clear')  
  print(logo + "\n")

# main game function
def game():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  my_cards = []
  pc_cards = []
  my_score = 0
  pc_score = 0

  # players draw their first card 
  my_cards.append(random.choice(cards))
  pc_cards.append(random.choice(cards))
  cont = "y"
  r = 1
  
  while cont == "y" and my_score <= 21:
    clear()    
    r += 1

    # players draw another random card
    my_cards.append(random.choice(cards))
    pc_cards.append(random.choice(cards))

    # adding the cards to calculate current score
    my_score = sum(my_cards)
    pc_score = sum(pc_cards)

    # if the player has an ace and their score is greater than 21, they can change the value of the ace from 11 to 1
    if my_score > 21:
      if 11 in my_cards:
        my_score -= 10
        i = my_cards.index(11)
        my_cards[i] = 1

    # displaying player's cards and score, and dealer's first card
    print(f"Your cards: {my_cards}\nYour score: {my_score}\n")
    print(f"Dealer's first card: {pc_cards[0]}\n\n")

    #asking the player if they want to draw another card
    if my_score < 22:
      cont = input("Type 'y' to draw, type 'n' to pass\n")
      print("\n")

  # exiting out of the loop because: the player either refused to draw another card, or went over
  clear()

  # displaying the players' final hands and scores
  print(f"Your final hand: {my_cards}\nYour final score: {my_score}\n")
  print(f"Dealer's final hand: {pc_cards}\nDealer's final score: {pc_score}\n\n")

  # displaying the results of the game  
  if my_score > 21:
    print("You went over. You lose!\n\n")
  else:
    if my_score == 21:
      print("Win with a BlackJack!\n\n")
    elif pc_score > 21:
      print("Opponent went over. You win!\n\n")
    elif my_score > pc_score:
      print("You win!\n\n")
    elif my_score < pc_score:
      print("You lose!\n\n")
    elif my_score == pc_score:
      print("It's a draw!\n\n")

  # prompt to ask player if they want to play again
  if input("Type 'y' to play again, 'n' to stop here.\n").lower() == 'y':
    game()
  else:
    _ = system('clear')

# starting the game
print(logo + "\n")
if input("Enter 'start' to play.\n").lower() == "start":
  game()
