import random,art
print(art.logo)

def deal_cards():
    cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    new_card=random.choice(cards)
    return new_card
def total_score(cards):
     if sum(cards)==21 and len(cards==2):
         return 0
     if 11 in cards and sum(cards)>21:
         cards.remove(11)
         cards.append(1)
     return sum(cards)
def compare(user,computer):
    if user==computer:
        return "Draw"
    elif computer==0:
        return "Opponent has blackjack. You lose"
    elif user==0:
        return "You win with a blackjack"
    elif user>21:
        return "You went over. You lose"
    elif computer>21:
        return "Opponent went over. You win"
    elif user>computer:
        return "You win"
    else:
        return "You lose"

def start_game():
    user_cards=[]
    comp_cards=[]

    comp_score=-1
    user_score=-1
    game_over=False

    for _ in range(2):
        user_cards.append(deal_cards())
        comp_cards.append(deal_cards())
    while not game_over:
        user_score=total_score(user_cards)
        comp_score=total_score(comp_cards)
        print(f"Your cards are:{user_cards},current score:{user_score}")
        print(f"Computer's first card is :{comp_cards[0]}")

        if user_score==0 or comp_score==0 or user_score>21:
            game_over=True
        else:
            more_cards=input("Type 'y' for another card or 'n' to pass")
            if more_cards=='y':
                user_cards.append(deal_cards())
            else:
                game_over=True
    while comp_score!=0 and comp_score<17:
        comp_cards.append(deal_cards())
        comp_score=total_score(comp_cards)

    print(f"Your final hand :{user_cards},final score:{user_score}")
    print(f"Computer's final hand:{comp_cards},final score:{comp_score}")
    print(compare(user_score,comp_score))

while (input("Do you wanna play blackjack? Type 'y' or 'n'"))=='y':
    start_game()
    



