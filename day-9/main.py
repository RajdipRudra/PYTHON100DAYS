import art
import os
asscii = art.logo

def chosing_winner(dic_val):
    names = []
    bids = []
    winner = ''
    for key in dic_val:
        names.append(key)
        bids.append(dic_val[key])
    higst_bid = max(bids)
    winner = names[bids.index(higst_bid)]
    return winner



dic_infos = {}
is_on = True

while is_on:
    #printing stuff
    print(asscii)
    print("Welcome to the secret auction program.")

    #input stuff
    user_name = input("What is your name?\n--> ")
    user_bid = float(input("What's your bid?\n--> "))

    #assinging values in a dic
    dic_infos[user_name] = user_bid

    #asking if there's another bidder
    another_bidder = input("are there any other bidders? type 'yes' or 'no'\n").lower()

    if another_bidder == 'no' or another_bidder =='n':
        winner_is = chosing_winner(dic_infos)
        print(f"the highest bid is {dic_infos[winner_is]} and the WINNER is {winner_is.upper()}")
        is_on = False
    else:
        os.system("clear")



