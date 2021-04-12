# n=18
# num1=int(input("Enter Your Number"))
#
# if n==num1:
#     print("Congrats You Won")
#     print("No of Guesses Left 9 ")
# else:
#     print("Game Over")

number = 18

guesses = 9

while guesses>0:
    inp = int(input("Enter the number: \n"))
    if inp == 18:
        print("YOU WON in",9-guesses + 1,"guesses!\n")
        break

    elif inp < 18:
        if (18-inp) <= 3:
            print("Thoda zyada karo.")
        else:
            print("Zyada karo.")

    elif inp > 18:
        if (inp-18) <= 3:
            print("Thoda kam karo.")
        else:
            print("Kam karo.")

    guesses = guesses-1
    print("You have", guesses, " guesses left.\n")
    if guesses == 0:
        print("GAME OVER! \nYOU LOST!")

