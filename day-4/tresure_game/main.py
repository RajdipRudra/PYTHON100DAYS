import os

stop =0

while stop==0:
    row1 = ['⬜️', '⬜️', '⬜️']
    row2 = ['⬜️', '⬜️', '⬜️']
    row3 = ['⬜️', '⬜️', '⬜️']

    map =[row1,row2,row3]
    print(f"{row1}\n{row2}\n{row3}\n")
    user_input = input("first enter the column , and then row-->")
    try:
        column = int(user_input[0])#2
        row = int(user_input[1])#3

        map[row-1][column-1] = "💰"
        print(f"{row1}\n{row2}\n{row3}\n")
        input()
        os.system('clear')


    except IndexError:
        stop=1