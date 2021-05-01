from art import logo
# print(logo)
import random

def restart_game():
  player_cards.clear()
  cpu_cards.clear()
  player_cards.append(random.choice(cards))
  cpu_cards.append(random.choice(cards))  
  hit_me()

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
cpu_cards = []

def hit_me():
  player_cards.append(random.choice(cards))
  if 11 in player_cards and sum(player_cards) > 21:
    player_cards.remove(11)
    player_cards.append(1)
  if sum(cpu_cards) <= 21:
     cpu_cards.append(random.choice(cards))
  if sum(player_cards) > 21 and len(player_cards) == 2:
    print(f"    Your cards are: {player_cards}. That's BLACKJACK. Congrats!")
  if sum(player_cards) > 21:
      print(f"    Your final hand: {player_cards}, final score: {sum(player_cards)}")
      print(f"    Computer's final hand: {cpu_cards}, final score: {sum(cpu_cards)}.")
      print("You went over. You lose. 😭")
      if input("Play again? 'y' ") == "y":
          restart_game()
      else:
        print("Thanks for playing!")
  if sum(player_cards) <= 21:
    print(f"    Your cards: {player_cards}, current score is {sum(player_cards)}.")
    print(f"    Computer's first card: {cpu_cards[0]}")
    next_please = input("Type 'y' to get another card, type 'n' to pass: ")
    if next_please == "n":
      if sum(player_cards) > sum(cpu_cards) and sum(cpu_cards) <= 21:
        print(f"    Your final hand: {player_cards}, final score: {sum(player_cards)}")
        print(f"    Computer's final hand: {cpu_cards}, final score: {sum(cpu_cards)}.")
        print("You win! 🤩")
        if input("Play again? 'y' ") == "y":
          restart_game()
        else: 
          print("Thanks for playing!")
      if sum(player_cards) <=21 and sum(cpu_cards) > 21:
        print(f"    Your final hand: {player_cards}, final score: {sum(player_cards)}")
        print(f"    Computer's final hand: {cpu_cards}, final score: {sum(cpu_cards)}.")
        print("You win! 🤩")
        if input("Play again? 'y' ") == "y":
          restart_game()
        else: 
          print("Thanks for playing!")
      else:
        print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
        print(f"Computer's final hand: {cpu_cards}, final score: {sum(cpu_cards)}.")
        print("You lose! 😭")
        if input("Play again? 'y' ") == "y":
          restart_game()
        else: 
          print("Thanks for playing!")
    if next_please == "y":
      hit_me()

if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  player_cards.append(random.choice(cards))
  cpu_cards.append(random.choice(cards))
  hit_me()
else:
  print("Well alright then!")





#TEST FROM FINISHED EXAMPLE
#    Your cards: [10, 6], current score: 16
#    Computer's first card: 3
# Type 'y' to get another card, type 'n' to pass: y
#    Your cards: [10, 6, 3], current score: 19
#    Computer's first card: 3
# Type 'y' to get another card, type 'n' to pass: n
#    Your final hand: [10, 6, 3], final score: 19
#    Computer's final hand: [3, 8, 9], final score: 20
# You lose 😤
# Do you want to play a game of Blackjack? Type 'y' or 'n': 
#
#IF YOU BUST
#    Computer's final hand: [7, 10], final score: 17
# You went over. You lose 😭


############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

