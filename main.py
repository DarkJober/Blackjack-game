import random
from art import logo
from replit import clear

#Function wich deal one card
def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#Function to calculate the score - input player or computer
def calculate_score(i):
    """Take a list of cards and return the score calculated by cards."""
    if sum(i) == 21 and len(i) == 2:
        return 0
    if 11 in i and sum(i) > 21:
            i.remove(11)
            i.append(1)
    return sum(i)

def compare(player_score, computer_score):
    if player_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has BlackJack."
    elif player_score == 0:
        return "Win, you have a BlackJack."
    elif player_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "You win. Opponent went over."
    elif player_score > computer_score:
        return "You win!"
    else:
        return "You lose :(. Computer had higher score."

def play_game():
    print(logo)
    
    player = []
    computer = []

    #Draw 2 cards to user and 2 cards to computer¨
    for _ in range(2):
        player.append(deal_card())   
        computer.append(deal_card())
    
    #Check if user or computer have blackjack (ace + 10)
    game = True
    
    while game:
        
        player_score = calculate_score(player)
        computer_score = calculate_score(computer)
        
        print(f"Your cards: {player}, your current score: {player_score}")
        print(f"Computer's first card: {computer[0]}")
        
        if player_score == 0 or computer_score == 0 or player_score > 21:
            game = False
        else:
            another_card = input("Do you want another card? 'y' or 'n' to pass: ")
            if another_card == "y":
                player.append(deal_card())
            else:
                game = False
                 
    while computer_score != 0 and computer_score < 17:
        computer.append(deal_card())
        computer_score = calculate_score(computer)
    
    print(f"    Your final hand: {player}, final score: {player_score}")
    print(f"    Computer final hand: {computer}, final score: {computer_score}")
    print(compare(player_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()