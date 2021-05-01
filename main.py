from art import logo
import random

# print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
cpu_cards = []

def hit_me():
  player_cards.append(random.choice(cards))
  if sum(cpu_cards) <= 21:
     cpu_cards.append(random.choice(cards))
  if sum(player_cards) > 21:
      print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
      print(f"Computer's final hand: {cpu_cards}, final score: {sum(cpu_cards)}.")
      print("You went over. You lose.")
  if sum(player_cards) <= 21:
    print(f"Your cards: {player_cards}, current score is {sum(player_cards)}.")
    print(f"Computer's first card: {cpu_cards[0]}")
    next_please = input("Type 'y' to get another card, type 'n' to pass: ")
    if next_please == "n":
      if {sum(player_cards)} > {sum(cpu_cards)}:
        print("YOU WIN YAY")
    if next_please == "y":
      hit_me()
  

  
  

player_cards.append(random.choice(cards))
cpu_cards.append(random.choice(cards))
hit_me()



######################################

# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# continue_game = True
# player_cards = []
# cpu_cards = []
# next_please = ""

# def hit_me():
#   '''
#   Adds another card to player and cpu hands.
#   '''
#   player_cards.append(random.choice(cards))
#   if sum(cpu_cards) <= 21:
#     cpu_cards.append(random.choice(cards))
#   while continue_game == True:
#     if sum(player_cards) > 21:
#       continue_game == False
#       print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
#       print(f"Computer's final hand: {cpu_cards}, final score: {sum(cpu_cards)}.")
#       print("You went over. You lose.")
#       break
#     if sum(player_cards) <= 21:
#       print(f"Your cards: {player_cards}, current score is {sum(player_cards)}.")
#       print(f"Computer's first card: {cpu_cards[0]}")
#       next_please = input("Type 'y' to get another card, type 'n' to pass: ")
#       if next_please == "y":
#         hit_me()
#       if next_please == "n":
#         continue_game == False
#         print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
#         print(f"Computer's final hand: {cpu_cards}, final score: {sum(cpu_cards)}.")
#         if {sum(player_cards)} > {sum(cpu_cards)}:
#           print("YOU WIN YAY")
#           break
#         else:
#           print("you lose BOOOO")
#           break

# player_cards.append(random.choice(cards))
# cpu_cards.append(random.choice(cards))
# hit_me()


###############################


# player_cards.append(random.choice(cards))
# player_cards.append(random.choice(cards))
# cpu_cards.append(random.choice(cards))
# cpu_cards.append(random.choice(cards))
# print(f"Yoyur cards: {player_cards}, current score is {sum(player_cards)}.")
# print(f"Computer's first card: {cpu_cards[0]}")
# next_please = input("Type 'y' to get another card, type 'n' to pass: ")
# if next_please == "y":
#   hit_me()
# if next_please == "n":
#   continue_game == False
#   print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
#   print(f"Computer's final hand: {cpu_cards}, final score: {sum(cpu_cards)}.")
#   if {sum(player_cards)} > {sum(cpu_cards)}:
#     print("YOU WIN YAY")
#   if {sum(cpu_cards)} > {sum(player_cards)}:
#     print("you lose BOOOO")
    

# def hit_me():
#   '''
#   Adds another card to player and cpu hands.
#   '''
#   player_cards.append(random.choice(cards))
#   if sum(cpu_cards) <= 21:
#     cpu_cards.append(random.choice(cards))
#   print(f"Your cards: {player_cards}, current score is {sum(player_cards)}.")
#   print(f"Computer's first card: {cpu_cards[0]}")
#   while continue_game == True:
#     if sum(player_cards) > 21:
#       continue_game == False
#       print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
#       print(f"Computer's final hand: {cpu_cards}, final score: {sum(cpu_cards)}.")
#       print("You went over. You lose.")
#     if sum(player_cards) <= 21:
#       next_please = input("Type 'y' to get another card, type 'n' to pass: n")
#       if next_please == "y":
#         hit_me()









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

