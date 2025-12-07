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

def addition(num1,num2):
    return num1+num2

def substraction(num1,num2):
    return num1-num2

def multiplication(num1,num2):
    return num1*num2

def division(num1,num2):
    return num1/num2


cal_dic = {
    "+":addition,
    "-":substraction,
    "*":multiplication,
    "/":division
}

def gives_ans(first_number,second_number,operation):
    ans = 0
    for key in cal_dic:
        if key == operation:
            ans = cal_dic[key](first_number,second_number)
    return ans

def calculation():
    print(art.logo)
    first_number = float(input("enter the first number\n-->"))
    operation = input("what operation do you wanna perform?{+,-,*,/}\n-->").lower()
    second_number = float(input("enter the second number\n-->"))
    ans = gives_ans(first_number,second_number,operation)
    # if operation=='+' or operation=="add":
    #     ans = addition(first_number,second_number)
    # elif operation=='-' or operation=="sub":
    #     ans = substraction(first_number,second_number)
    # elif operation=='*' or operation=="mul":
    #     ans = multiplication(first_number,second_number)
    # elif operation=='/' or operation=="div":
    #     ans = division(first_number,second_number)

    logo = logo_print(first_number,second_number,ans,operation)
    for i in logo:
        print(i)
    is_on = True
    while is_on == True:
        continueee = input(f"do you wanna continue calculation with previous calculation ans{ans}? yes(y) or no(n)").lower()
        if continueee=="y" or continueee=="yes":
            first_number = ans
            operation = input("what operation do you wanna perform?{+,-,*,/}\n-->").lower()
            second_number = float(input("enter the second number\n-->"))
            ans = gives_ans(first_number,second_number,operation)
            logo = logo_print(first_number,second_number,ans,operation)
            for i in logo:
                print(i)

        elif continueee=='n' or continueee=="no":
            is_on = False
            calculation()

calculation()
