import random
#gen random 4digits number
str_gen_num = str(random.randint(1000, 9999))

print("[debug] random generated: ", str_gen_num)
print("Welcome to the A and B Game and a 4-digit number is generated.")

c = 1
while True:
    usr_input = input("Please guess a 4-digit number:")
    
    if usr_input == 'exit':
        usr_input = None
        print("Thanks for playing, goodbye!")
        break
    elif type(usr_input) == int or len(usr_input) == 4:
        str_input = str(usr_input)
        if str_input == str_gen_num:
            print("YOU GUESSED THE CORRECT NUMBER HURRAY!!!!!")
            print("IT IS: ", str_gen_num)
            print("YOU TRIED :", c, "TIMES W0W")
            break
        else:
            c += 1 #counting
            a, b = 0, 0
            for i in range(4):
                if str_input[i] == str_gen_num[i]:  #correct num and place
                    a += 1
                if ((str_input[i] != str_gen_num[i]) & (str_input[i] in str_gen_num)):#correct num but not place
                    b += 1

            print("You guess:", str_input)
            print("A: ", a, "B:", b)      
    else:
        print("Invalid input, please try again")
        
