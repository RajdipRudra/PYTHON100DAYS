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




# def is_21_or_not(sum_user,sum_comp,user_cards):
#     if sum_comp==21 or sum_user==21:
#         if sum_user==21:
#             print(f"U WIN\ncomp-->{comp_cards}\nuser-->{user_cards}")
#             return 1
#         elif sum_comp==21:
#             print(f"COMP WIN\ncomp-->{comp_cards}\nuser-->{user_cards}")
#             return 0


#     while sum_user>21 and 11 in user_cards:
#         indexx = user_cards.index(11)
#         user_cards[indexx] = 1
#         sum_user = sum(user_cards)
#     if sum(user_cards)>21:
#         print(f"COMPP WINN\ncomp-->{comp_cards}\nuser-->{user_cards}")


#     return None

# def win_who():
#     if sum(comp_cards)==sum(user_cards):
#         print("it's a fucking tie")
#     elif sum(comp_cards)>21 and sum(user_cards)>21:
#         print("both got busted")

#     elif sum_user > 21 or (sum_comp <= 21 and sum_comp > sum_user):
#         print(f"COMPPP WONN\ncomp-->{comp_cards}\nuser-->{user_cards}")
#     else:
#         print(f"U WON\ncomp-->{comp_cards}\nuser-->{user_cards}")

# def deal_card():
# #                                  J, Q, K
#     cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
#     return rn.choice(cards)
# logo = art.logo
# print(logo)
# comp_win = 0
# user_win = 0
# #user_card created and 2 card assinged
# user_cards = []
# for i in range(2):
#     user_cards.append(deal_card())

# #comp_card created and 2 card assinged
# comp_cards = []
# for j in range(2):
#     comp_cards.append(deal_card())

# game_is_on = True
# while game_is_on== True:
    # print(user_cards,comp_cards)

    # user_draw_card = input("do u wanna draw another card? 'y' or 'n' ").lower()

    # sum_user = sum(user_cards)
    # sum_comp = sum(comp_cards)

    # if user_draw_card == 'y':

    #     user_cards.append(deal_card())
    #     #sum of comp and user
    #     sum_comp = sum(comp_cards)
    #     sum_user = sum(user_cards)

    #     user_win = is_21_or_not(sum_user=sum_user,sum_comp=sum_comp,user_cards=user_cards)
    #     while sum(comp_cards)<17:
    #         comp_cards.append(deal_card())
    #     if user_win != None:
    #         game_is_on = False
    

    # elif user_draw_card=='n':
    #     is_21_or_not(sum_user=sum_user,sum_comp=sum_comp,user_cards=user_cards)
    #     while sum(comp_cards)<17:
    #         comp_cards.append(deal_card())
    #     win_who()
    #     game_is_on = False


#tutorial projecct
import art
import random as rn
import os


#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = rn.choice(cards)
  return card

def calculate_score(cards):
                                #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
                                
# if 11 in cards and 10 in cards and len(cards) == 2:
    if sum(cards) ==21 and len(cards)==2:
       return 0
                                #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in cards and sum(cards)>21:
       cards.remove(11)
       cards.append(1)

    return sum(cards)
                                #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.





def compare(comp_score,user_score):

    if user_score==comp_score:
        return "Draw"
    elif comp_score==0:
        return "Lose, Opponent has Blackjack"
    elif user_score==0:
        return "Win with a blackjack"
    elif user_score>21:
        return "went over, You lose"
    elif comp_score>21:
        return "Opponent Won"
    elif user_score>comp_score:
        return "YOU WIN"
    else:
        return "YOU LOSE"
    

def play_game():

    print(art.logo)

    #Hint 5: Deal the user and computer 2 cards each using deal_card()
    is_game_over = False
    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    user_score = calculate_score(user_cards)
    comp_score = calculate_score(computer_cards)




    #Hint 6: Create a function called calculate_score() that takes a List of cards as input 
    #and returns the score. 
    #Look up the sum() function to help you do this.




    while not is_game_over:
        print(f"user score--->{user_cards}, current score: {user_score}\nComp score---> {computer_cards[0]}")
        if user_score == 0 or comp_score==0 or user_score>21:
            is_game_over = True
        else:
            another_card = input("type 'y' to get another card, type 'n' to pass:\n").lower()
            if another_card=='y':
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
            else: 
                is_game_over = True
        


    while comp_score != 0 and comp_score<17:
        computer_cards.append(deal_card())
        comp_score = calculate_score(computer_cards)


    print(f"yyour final hand is this {user_cards} and ur hand is {user_score}")
    print(f"cOmputer final hand is this {computer_cards} and ur hand is {comp_score}")
    print(compare(comp_score,user_score))

    continuee = input("do you want to play a game of blackjack 'y' or 'n' : ").lower()
    if continuee=='y':
        os.system("clear")
        play_game()
    else:
        is_game_over = True


play_game()