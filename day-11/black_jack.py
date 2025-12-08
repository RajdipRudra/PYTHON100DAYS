############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.


##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.


#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
    
#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

    
#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    
#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

        
#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.



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










import art
import random as rn


logo = art.logo
#                               J, Q, K
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]


#Deal both user and computer a starting hand of 2 random card values.
def gen_card_start(cards):
    rn_2cards = []
    for i in range(2):
        rn_2cards.append(rn.choice(cards))
    return rn_2cards

def gen_acard(cards,cards_of_userr):
    rn_acard= rn.choice(cards)
    if rn_acard == 11 and sum(cards_of_userr)+ 11 >21:
        rn_acard = 1

    return rn_acard 


def if_computer_gen(comp_cards):
    if sum(comp_cards)<17:
        return gen_acard(cards,comp_cards)
    return None



print(logo)




def who_wins(user_cards,comp_cards):
    user_sum = sum(user_cards)
    comp_sum = sum(comp_cards)
    if user_sum > 21 and comp_sum > 21:
        print("Both busted! It's a tie 🤝")
    elif user_sum == comp_sum:
        print("IT'S A TIE 😐")

    # User busts
    elif user_sum > 21:
        print("You busted! Computer wins 😭")

    # Computer busts
    elif comp_sum > 21:
        print("Computer busted! You win 😎")

    # Higher score wins
    elif user_sum > comp_sum:
        print("You win! 🔥")
    else:
        print("Computer wins 😤")
    

    

def game_is_on():
    user_cards = gen_card_start(cards)

    computer_cards = gen_card_start(cards)

    is_gameon = True
    while is_gameon:
        if sum(user_cards) < 21:


            print(f"Your cards: {user_cards}")
            print(f"Computer's first card: {computer_cards[0]}")
            draw_another = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if draw_another == 'y':
                user_cards.append(gen_acard(cards,user_cards))
                new_comp = if_computer_gen(computer_cards)
                if new_comp is not None:
                    computer_cards.append(new_comp)
            else:
                who_wins(user_cards,computer_cards)
                wanna_playagain = input("DO YOU WANT TO PLAY A GAME OF BLACKJAKE? (y) or (n)").lower()
                if wanna_playagain == 'n':
                    is_gameon = False
                else:
                    game_is_on()
        else:
            who_wins(user_cards,computer_cards)
            wanna_playagain = input("DO YOU WANT TO PLAY A GAME OF BLACKJAKE? (y) or (n)").lower()
            if wanna_playagain == 'n':
                    is_gameon = False
            else:
                game_is_on()


game_is_on()