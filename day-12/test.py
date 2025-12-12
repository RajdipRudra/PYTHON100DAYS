import random as rn

logo = '''
 _____       _____          _____ _            _   _                 _     ___________ 
│  __ ╲     │  ___│        │_   _│ │          │ ╲ │ │               │ │   │  ___│ ___ ╲
│ │  ╲╱_   _│ │__ ___ ___    │ │ │ │__   ___  │  ╲│ │_   _ _ __ ___ │ │__ │ │__ │ │_╱ ╱
│ │ __│ │ │ │  __╱ __╱ __│   │ │ │ '_ ╲ ╱ _ ╲ │ . ` │ │ │ │ '_ ` _ ╲│ '_ ╲│  __││    ╱ 
│ │_╲ ╲ │_│ │ │__╲__ ╲__ ╲   │ │ │ │ │ │  __╱ │ │╲  │ │_│ │ │ │ │ │ │ │_) │ │___│ │╲ ╲ 
 ╲____╱╲__,_╲____╱___╱___╱   ╲_╱ │_│ │_│╲___│ ╲_│ ╲_╱╲__,_│_│ │_│ │_│_.__╱╲____╱╲_│ ╲_│
                                                                                       
                                                                                       
                                                                                       
                                                                                       '''

 

print("Welcome to the Number Guessing Game!")

EASY = 10
HARD = 5

def win_conditions(Guessed_num,user_input,life):

    if user_input==Guessed_num :
        return f"You got it! The answer was {Guessed_num}\n"
    elif user_input< Guessed_num :
        if life>1:
            return "Too low.\nGuess again.\n"
        else:
            return "Too low.\n"
        
    elif user_input> Guessed_num :
        if life>1:
            return "Too HIGH.\nGuess again.\n"
        else:
            return "Too HIGH.\n"

def game_on(lifes,Guessed_num):
    life =lifes
    while life != 0:
        print(f"You have {life} attempts remaining to guess the number.")
        user_input = int(input("Make a guess --> "))
        win_or_not = win_conditions(Guessed_num=Guessed_num,user_input=user_input,life=life)
        if win_or_not==f"You got it! The answer was {Guessed_num}\n":
            print(win_or_not)
            break
        else:
            life -= 1
            print(win_or_not)
    if life==0:
        print(f"YOU LOSE!! THE NUMBER WAS {Guessed_num}")

print(logo)
print("I'm thinking of a number between 1 and 100.")
Guessed_num = rn.randint(1,100)
Difficulty = input("Choose a difficulty. Type 'easy' or 'hard':  ").upper()

if Difficulty == "HARD":
    game_on(HARD,Guessed_num)
elif Difficulty == "EASY":
    game_on(EASY,Guessed_num)












 