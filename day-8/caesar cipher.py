art = [
"                                                                                                    ",
"                                                                                                    ",
"                                                                                                    ",
"                                                                                                    ",
"                    3                           1  7    31     277                                  ",
"                   73900980940989068000841      63 61     50000900000000800080851                   ",
"                       159808980008089007       68009      900800000990000951                       ",
"                          719008060089009432543590800966448080000000000957                          ",
"                             77600808888000009088800008000069000000082                              ",
"                                 33080000080990899000080009000000057                                ",
"                                   8900080099400090000060000008808                                  ",
"                                   00008847   300000005   729000007                                 ",
"                                  59857        80009807       73497                                 ",
"                                               4008905                                               ",
"                                                000007                                               ",
"                                                90009                                                ",
"                                                30007                                                ",
"                                                 908                                                 ",
"                                                 304                                                 ",
"                                                  97                                                 ",
"                                                  3                                                  ",
"                                                                                                    ",
]


for i in art:
    print(fr"{i}")


import time

Charecters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',"0","1","2","3","4","5","6","7","8","9",' ','!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',"0","1","2","3","4","5","6","7","8","9",' ','!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?']

def str_to_list(msg):
    msg_list = []
    for i in msg:
        msg_list.append(i)
    return msg_list





def encrypt(message,shift_number):
    message_in_list = str_to_list(message)
    encrypt_msg = []
    for i in range(len(message_in_list)):
        for j in range(len(Charecters)):
            if message_in_list[i]==Charecters[j]:
                encrypt_msg.append(Charecters[j+shift_number])
                break
    return encrypt_msg




def decrypt(message,shift_number):
    message_in_list = str_to_list(message)
    encrypt_msg = []
    for i in range(len(message_in_list)):
        for j in range(len(Charecters)):
            if message_in_list[i]==Charecters[j]:
                encrypt_msg.append(Charecters[j-shift_number])
                break
    return encrypt_msg


is_on = True

while is_on==True:
    en_de = input("TYPE 'EN' TO ENCRYPT OR 'DE' TO DECRYPT AND 'ESC' TO ESCAPE -->\n").upper()
    if en_de == 'EN':
        the_msg_input = input("enter the msg here--> ")
        the_shift_number = int(input("enter the shift number --> "))
        encrypt_msg = encrypt(message=the_msg_input,shift_number=the_shift_number)
        print(f"The encryped msg is -->\n{"".join(encrypt_msg)}")
        time.sleep(10)

    elif en_de == 'DE':
        the_msg_input = input("enter the msg here--> ")
        the_shift_number = int(input("enter the shift number --> "))
        decrypt_msg = decrypt(message=the_msg_input,shift_number=the_shift_number)
        print(f"The encryped msg is -->\n{"".join(decrypt_msg)}")
        time.sleep(10)
    elif en_de=="ESC":
        is_on==False
        break
    
