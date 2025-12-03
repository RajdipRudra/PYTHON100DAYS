'''def prime_number_check(number):
    for i in range(2,number):
        if number%i!=0 and number%number==0:
            # print(i)
            print(f"{number} its a prime number")
            
        else:
            print(number)
            print("not prime")

n = int(input("Check this number : "))
prime_number_check(number=n)'''


def prime_number_check(number):
    is_prime = False
    for i in range(2,number):
        if number==0 or number==1 or number==2:
            print("enter a valid number it's not acceptable")
            break
            
        elif number%i!=0 and number%number==0:
            is_prime = True
                    
        elif number%i==0:
            is_prime = False
            break
    
    if is_prime is True:
        print(f"The number {number} is a Prime Number")
    else:
        print(f"The number {number} is-NOT a Prime Number")

n = int(input("Check this number : "))
prime_number_check(number=n)