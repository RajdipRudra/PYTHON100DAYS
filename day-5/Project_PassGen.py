import random as rn

Upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

Lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

Letters = [Upper,Lower]


Numbers = ["0","1","2","3","4","5","6","7","8","9"]

Acceptable_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?']



print("Welcome to the PyPassword Generator!")

letter_want = int(input("How manny letters would you like in your password?\n"))
Num_want = int(input("How manny Numbers would you like in your password?\n"))
SpecialC_want = int(input("How manny Special-Chara would you like in your password?\n"))

gen_letters = []
for i in range(letter_want):
    gen_letters.append(rn.choice(Letters[rn.randint(0,1)]))
gen_L = "".join(gen_letters)


gen_Numbers = []
for i in range(Num_want):
    gen_Numbers.append(rn.choice(Numbers))
gen_N = "".join(gen_Numbers)

gen_sc = []
for i in range(SpecialC_want):
    gen_sc.append(rn.choice(Acceptable_chars))
gen_SC = "".join(gen_sc)

pass_wd = [gen_L,gen_N,gen_SC]

PassWorD = []
for i in pass_wd:
    for j in i:
        PassWorD.append(j)

rn.shuffle(PassWorD)
passs = "".join(PassWorD)





print(f"Your Password is -->\n{passs}")

input()