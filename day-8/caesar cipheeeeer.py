'''def prime_number_check(number):
    for i in range(2,number):
        if number%i!=0 and number%number==0:
            # print(i)
            print(f"{number} its a prime number")
            
        else:
            print(number)
            print("not prime")

n = int(input("Check this number : "))
prime_number_check(number=n)


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
prime_number_check(number=n)'''



Charecters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',"0","1","2","3","4","5","6","7","8","9",' ','!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',"0","1","2","3","4","5","6","7","8","9",' ','!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?']

def str_to_list(msg):
    msg_list = []
    for i in msg:
        msg_list.append(i)
    return msg_list

def encrypt(message,shift_number):
    message_in_list = str_to_list(message)
    encrypt_msg = []
    for i in message_in_list:
        for j in Charecters:
            if i==j:
                encrypt_msg.append(Charecters[shift_number])
    return encrypt_msg

def decrypt(message,shift_number):
    pass



encrypt_word = encrypt(message="i love sushi",shift_number=5)
print(encrypt_word)