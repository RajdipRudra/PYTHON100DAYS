
'''
import time, sys

def type_out(text, delay=0.08):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

lyrics = [
    "Lock me up and throw away the key",
    "He knows how to get the best out of me",
    "I'm no force for the world to see",
    "Trade my whole life just to be",
    "Top of the world but I'm still not free",
    "It's such a secret that I keep",
    "Until it's gone, I can never find peace",
    "Brace my whole life just to be"
]

for line in lyrics:
    type_out("\n"+line)

print("\n")'''


'''def is_leapyear(year):
    if year%4==0:
        if year%100:
            if year%400:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year,month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leapyear(year=year) and month==1:
        return 29
    else:
        return days_in_month[month]




year = int(input("enter ur year : "))
month = int(input("enter a month: "))
dats = days_in_month(year,(month-1))
print(dats)


def is_leapyear(year):
    if year%4==0:
        if year%100:
            if year%400:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year,month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leapyear(year=year) and month==1:
        return 29
    else:
        return days_in_month[month]




year = int(input("enter ur year : "))
month = int(input("enter a month: "))
dats = days_in_month(year,(month-1))
print(dats)
def is_leapyear(year):
    if year%4==0:
        if year%100:
            if year%400:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year,month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leapyear(year=year) and month==1:
        return 29
    else:
        return days_in_month[month]




year = int(input("enter ur year : "))
month = int(input("enter a month: "))
dats = days_in_month(year,(month-1))
print(dats)'''


#mport art
'''import random as rn


#logo = art.logo
#                               J, Q, K
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]


#Deal both user and computer a starting hand of 2 random card values.
''''''def gen_card_start(cards):
    rn_2cards = []
    for i in range(2):
        rn_2cards.append(rn.choice(cards))
    return rn_2cards'''

'''def gen_acard(cards):
    rn_acard= rn.choice(cards)
    return rn_acard 


def if_computer_gen(comp_cards):
    if sum(comp_cards)<17:
        return gen_acard(cards)



#print(logo)




def who_wins(user_cards,comp_cards):
    user_sum = sum(user_cards)
    comp_sum = sum(comp_cards)
    if (user_sum == comp_sum) or (user_sum>21 and comp_sum>21):
        print("IT's A TIE")
    elif ((user_sum<=21) and (user_sum>comp_sum))or ((user_sum<=21) and (user_sum<comp_sum)) or ((user_sum<21) and (comp_sum>=21)):
        print(f"U WIN\ncompcards{comp_cards}")
    elif ((comp_sum<=21) and (comp_sum>user_sum)) or ((user_sum<=21) and (user_sum>comp_sum)) or  ((user_sum>21) and (comp_sum<=21)):
        print(f"COMPUTER WINS{comp_cards}")
    

    


user_cards = [5,6,10]

computer_cards = [10,2,11]

is_gameon = True
while is_gameon:
    if ((sum(user_cards)!=21)) or ((sum(computer_cards)!=21 )):


        print(f"Your cards: {user_cards}")
        print(f"Computer's first card: {computer_cards}")
        draw_another = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if draw_another == 'y':
            user_cards.append(gen_acard(cards))

            computer_cards.append(if_computer_gen(computer_cards))
        else:
            who_wins(user_cards,computer_cards)
            wanna_playagain = input("DO YOU WANT TO PLAY A GAME OF BLACKJAKE? (y) or (n)").lower()
            if wanna_playagain == 'n':
                is_gameon = False
'''

no7_list = [
    "Structure", 
    '101', 
    "Algorithm", 
    "3.14", 
    "Python", 
    '15', 
    "Coding", 
    '99',
    "Coding", 
    '99', 
    "Structure", 
    '15',
    "Mode", 
    '1.618', 
    "List", 
    '20', 
    "Tuple", 
    '55'

]

for i in range(len(no7_list)):
    for j in range(len(no7_list)):
        if no7_list.count(no7_list[i])>=2:
            no7_list.pop(no7_list.index(no7_list[i]))
            
no7_list
    