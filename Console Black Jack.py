from random import *


indicator = "y"
continue_playing = "y"

cards = ["2","3","4","5","6","7","8","9","Queen","Jack","King","10","Ace"]

def score(score,card,live_indicator):

    if card == "Jack" or card == "Queen" or card == "King":
        score+=10
    elif card == "Ace" and score + 11 <= 21 and live_indicator == 1:
        score = ace_value(score)
    elif card == "Ace" and score + 11 > 21:
        score +=1
    elif card == "Ace" and score + 11 <= 21 and live_indicator == 0:
        score+=11
    else:
        score+=int(card)

    return score

def gamestart():
    user_cards = []
    computer_cards = []
    user_score = 0
    computer_score = 0

    for i in range(2):
        user_score = user_append(user_score, user_cards, 0)
        computer_score = computer_append(computer_score, computer_cards)
    return user_cards, computer_cards, user_score, computer_score



def gameplay(user_cards, computer_cards, user_score, computer_score):

    print(f"\nComputer first card {computer_cards[0]}")
    indicator = input(f"Your cards {', '.join(user_cards)}, and your score {user_score}, do you want to take one more card? ('y'/'n')  ")
    while computer_score < 17:
        computer_score = computer_append(computer_score, computer_cards)
    while indicator == "y" and user_score <= 21:
        user_score = user_append(user_score,user_cards, 1)
        indicator = indicator_value(user_score,computer_score)

    return user_cards, computer_cards, user_score, computer_score



def computer_append(computer_score,computer_cards):
    computer_card = cards[randint(0, len(cards) - 1)]
    computer_cards.append(computer_card)
    computer_score = score(computer_score, computer_card, 0)
    return computer_score



def user_append(user_score,user_cards,live_indicator):
    user_card = cards[randint(0, len(cards) - 1)]
    user_cards.append(user_card)
    user_score = score(user_score, user_card, live_indicator)
    return user_score




def indicator_value(user_score, computer_score):
    if user_score > 21:
        indicator = "n"
    # elif computer_score <= 21 and user_score > 21:
    #     indicator = "n"
    # else:
    else:
        indicator = input(f"Your cards {', '.join(user_cards)}, and your score {user_score}, do you want to take one more card? ('y'/'n')  ")
    return indicator



def printer(user_cards, computer_cards, user_score, computer_score):

    if user_score > 21 and computer_score <= 21 or user_score < computer_score and computer_score <= 21:
        continue_playing = input(f"You lose... Your cards {', '.join(user_cards)}, and your score {user_score}. Computer cards {', '.join(computer_cards)}, and computer score {computer_score}\n Do you want to continue playing? ('y'/'n'): ")
    elif user_score > 21 and computer_score > 21 or user_score == computer_score:
        continue_playing = input(f"Draw... Your cards {', '.join(user_cards)}, and your score {user_score}. Computer cards {', '.join(computer_cards)}, and computer score {computer_score}\n Do you want to continue playing? ('y'/'n'): ")
    elif user_score <= 21 and computer_score > 21 or user_score > computer_score and user_score <= 21:
        continue_playing = input(f"You WIN!!! Your cards {', '.join(user_cards)}, and your score {user_score}. Computer cards {', '.join(computer_cards)}, and computer score {computer_score}\n Do you want to continue playing? ('y'/'n'): ")

    if continue_playing == "n":
        print("Good luck!")

    return continue_playing
def ace_value(score):
    ace_value = input(
        f"Your next card is Ace\nChoose your Ace value ('1'(your score {score + 1})/'11'(your score {score + 11})): ")
    while ace_value.isdigit() == 0 or int(ace_value) != 1 and int(ace_value) != 11:
        ace_value = input("Ace value ('1'/'11'): ")
    if int(ace_value) == 1:
        score += 1
    else:
        score += 11
    return score




logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

print(logo)

while continue_playing == "y":


    user_cards, computer_cards, user_score, computer_score = gamestart()

    user_cards, computer_cards, user_score, computer_score = gameplay(user_cards, computer_cards, user_score, computer_score)

    continue_playing = printer(user_cards, computer_cards, user_score, computer_score)


