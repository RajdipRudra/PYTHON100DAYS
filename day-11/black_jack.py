# import art
# import random as rn
# logo = art.logo
# #                               J, Q, K
# cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
# #Deal both user and computer a starting hand of 2 random card values.
# def gen_card_start(cards):
#     rn_2cards = []
#     for i in range(2):
#         rn_2cards.append(rn.choice(cards))
#     return rn_2cards

# def gen_acard(cards,cards_of_userr):
#     rn_acard= rn.choice(cards)
#     if rn_acard == 11 and sum(cards_of_userr)+ 11 >21:
#         rn_acard = 1

#     return rn_acard 
# def if_computer_gen(comp_cards):
#     if sum(comp_cards)<17:
#         return gen_acard(cards,comp_cards)
#     return None
# print(logo)
# def who_wins(user_cards,comp_cards):
#     user_sum = sum(user_cards)
#     comp_sum = sum(comp_cards)
#     if user_sum > 21 and comp_sum > 21:
#         print("Both busted! It's a tie 🤝")
#     elif user_sum == comp_sum:
#         print("IT'S A TIE 😐")

#     # User busts
#     elif user_sum > 21:
#         print("You busted! Computer wins 😭")

#     # Computer busts
#     elif comp_sum > 21:
#         print("Computer busted! You win 😎")

#     # Higher score wins
#     elif user_sum > comp_sum:
#         print("You win! 🔥")
#     else:
#         print("Computer wins 😤")
# def game_is_on():
#     user_cards = gen_card_start(cards)

#     computer_cards = gen_card_start(cards)

#     is_gameon = True
#     while is_gameon:
#         if sum(user_cards) < 21:


#             print(f"Your cards: {user_cards}")
#             print(f"Computer's first card: {computer_cards[0]}")
#             draw_another = input("Type 'y' to get another card, type 'n' to pass: ").lower()
#             if draw_another == 'y':
#                 user_cards.append(gen_acard(cards,user_cards))
#                 new_comp = if_computer_gen(computer_cards)
#                 if new_comp is not None:
#                     computer_cards.append(new_comp)
#             else:
#                 who_wins(user_cards,computer_cards)
#                 wanna_playagain = input("DO YOU WANT TO PLAY A GAME OF BLACKJAKE? (y) or (n)").lower()
#                 if wanna_playagain == 'n':
#                     is_gameon = False
#                 else:
#                     game_is_on()
#         else:
#             who_wins(user_cards,computer_cards)
#             wanna_playagain = input("DO YOU WANT TO PLAY A GAME OF BLACKJAKE? (y) or (n)").lower()
#             if wanna_playagain == 'n':
#                     is_gameon = False
#             else:
#                 game_is_on()
# game_is_on()



import art
import random as rn



def is_21_or_not(sum_user,sum_comp,user_cards):
    if sum_comp==21 or sum_user==21:
        if sum_user==21:
            print(f"U WIN\ncomp-->{comp_cards}\nuser-->{user_cards}")
            return 1
        elif sum_comp==21:
            print(f"COMP WIN\ncomp-->{comp_cards}\nuser-->{user_cards}")
            return 0


    while sum_user>21 and 11 in user_cards:
        indexx = user_cards.index(11)
        user_cards[indexx] = 1
        sum_user = sum(user_cards)
    if sum(user_cards)>21:
        print(f"COMPP WINN\ncomp-->{comp_cards}\nuser-->{user_cards}")


    return None



def win_who():
    if sum(comp_cards)==sum(user_cards):
        print("it's a fucking tie")
    elif sum(comp_cards)>21 and sum(user_cards)>21:
        print("both got busted")

    elif sum_user > 21 or (sum_comp <= 21 and sum_comp > sum_user):
        print(f"COMPPP WONN\ncomp-->{comp_cards}\nuser-->{user_cards}")
    else:
        print(f"U WON\ncomp-->{comp_cards}\nuser-->{user_cards}")





def deal_card():
#                                  J, Q, K
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return rn.choice(cards)


logo = art.logo
print(logo)

comp_win = 0
user_win = 0

#user_card created and 2 card assinged
user_cards = []
for i in range(2):
    user_cards.append(deal_card())

#comp_card created and 2 card assinged
comp_cards = []
for j in range(2):
    comp_cards.append(deal_card())




game_is_on = True
while game_is_on== True:
    print(user_cards,comp_cards)

    user_draw_card = input("do u wanna draw another card? 'y' or 'n' ").lower()

    sum_user = sum(user_cards)
    sum_comp = sum(comp_cards)

    if user_draw_card == 'y':

        user_cards.append(deal_card())
        #sum of comp and user
        sum_comp = sum(comp_cards)
        sum_user = sum(user_cards)

        user_win = is_21_or_not(sum_user=sum_user,sum_comp=sum_comp,user_cards=user_cards)
        while sum(comp_cards)<17:
            comp_cards.append(deal_card())
        if user_win != None:
            game_is_on = False
    

    elif user_draw_card=='n':
        is_21_or_not(sum_user=sum_user,sum_comp=sum_comp,user_cards=user_cards)
        while sum(comp_cards)<17:
            comp_cards.append(deal_card())
        win_who()
        game_is_on = False

