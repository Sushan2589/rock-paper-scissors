
def main():
    import random
    
    print("\033[1m"+"1 for Rock\n2 for Paper\n3 for Scissors")#"\033[1m"+"text"bolds the text
    user_input=int(input("What do you want to play(1-3)"))


    computer_input=random.randint(1,3)

    if user_input == computer_input:
        print("Its a draw\n")
        main()

    elif user_input==1 and computer_input==2:
        print("Not your game..Computer wins\n")

    elif user_input==1 and computer_input==3:
        print("Congratulations! You win\n")

    elif user_input==2 and computer_input==1:
        print("Congratulations! You win\n")

    elif user_input==2 and computer_input==3:
        print("Not your game..Computer wins\n")

    elif user_input==3 and computer_input==1:
        print("Not your game..Computer wins\n")

    elif user_input==3 and computer_input==2:
        print("Congratulations! You win\n")

    else:
        print("seems like you entered a invalid number!")
        again=input("Want to restart(Y/N)?:")
        if again.upper()=="Y":
            main()
        else:
            print("Thank you for playing")
            exit()
            
    game_again=input("Want to restart(Y/N)?:")
    if game_again.upper()=="Y":
            main()
    else:
            print("Thank you for playing")
            exit()

main()
