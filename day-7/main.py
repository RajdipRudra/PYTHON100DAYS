import random as rn
import os
import hangman_art,hangman_words

logo = hangman_art.logo
stagess = hangman_art.stages



def turn_dash(word):
    dash_list = []
    for i in word:
        dash_list.append("_")
    return dash_list


def check_word(dashed_word,word,user_input):
    word_list = []
    for wD  in word:
        word_list.append(wD)

    for i in range(len(word_list)):
        if user_input==word_list[i]:
            dashed_word[i]=user_input
    return dashed_word





is_game_on = True

Word = rn.choice(hangman_words.word_list).lower()

# Word = 'banana'
dashed_word = turn_dash(Word)
Life = len(stagess)-1

while is_game_on==True:

    os.system("clear")

    print(logo)

    print(stagess[Life])

    if Life>0:
        print(f"Life's Left--> {" ❤️ "*Life}")
        print("\n")
        print("  ".join(dashed_word))
        print("\n\n")
        
        user_input = input("Guess a letter -> ").lower()

        if user_input in Word:
            dashed_word = check_word(dashed_word=dashed_word,word=Word,user_input=user_input)
            if Word=="".join(dashed_word):
                is_game_on = False
                os.system("clear")
                print(f"\nThe word was --> {"".join(dashed_word)}")
                print("\nYOU SAVED THE HANG-MAN\n")
                input()

        else:
            Life -= 1
            
    else:
        is_game_on = False
        print("THE HANG-MAN IS DEAD\n")
        