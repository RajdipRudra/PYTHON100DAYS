import art
import os
logo_print = art.logo


def logo_print(num1,num2,ans,sign):
    logo = [ 
    fr" ___________________________",
    fr"|  _______________________  |",
    fr"|                           |",
    f"|    {num1} {sign} {num2} = {ans}       |",
    fr"|  _______________________  |",
    fr"|       ___ ___ ___   ___   |", 
    fr"|      | 7 | 8 | 9 | | + |  |", 
    fr"|      |___|___|___| |___|  |", 
    fr"|      | 4 | 5 | 6 | | - |  |", 
    fr"|      |___|___|___| |___|  |", 
    fr"|      | 1 | 2 | 3 | | x |  |", 
    fr"|      |___|___|___| |___|  |", 
    fr"|      | . | 0 | = | | / |  |", 
    fr"|      |___|___|___| |___|  |",  
    fr"|___________________________|"
    ]
    return logo


is_on = True

def addition(num1,num2):
    return num1+num2

def substraction(num1,num2):
    return num1-num2

def multiplication(num1,num2):
    return num1*num2

def division(num1,num2):
    return num1/num2


while is_on:
    print(art.logo)
    first_number = float(input("enter the first number\n-->"))
    operation = input("what operation do you wanna perform?{+,-,*,/}\n-->").lower()
    second_number = float(input("enter the second number\n-->"))
    ans = 0
    if operation=='+' or operation=="add":
        ans = addition(first_number,second_number)
    elif operation=='-' or operation=="sub":
        ans = substraction(first_number,second_number)
    elif operation=='*' or operation=="mul":
        ans = multiplication(first_number,second_number)
    elif operation=='/' or operation=="div":
        ans = addition(first_number,second_number)
    
    logo = logo_print(first_number,second_number,ans,operation)
    for i in logo:
        print(i)
    continueee = input("do you wanna continue calculation? yes(y) or no(n)").lower()
    if continueee=='n' or continueee=="no":
        is_on = False
    os.system('clear')



