import random

repeat = "YES"
while (repeat ==  "YES"):
    guess = random.randint(1,10)
    name = input("whats your name heyy!!")
    print(f"\nSo {name} I AM A MONSTER giving you only 3 chances to guess the number")
    no_guesses = 0

    while(no_guesses<=2):
        print(f"\nYou have {3 - no_guesses} chances left")
        choice = int(input(f"Guess now!!"))
        if (choice == guess):
            print("WOW YOU GOT IT!! YOU ARE SAVED BYEE!!")
        else:
            if(no_guesses == 2):
                print(f'WRONG,EATING YOU!! correct answer is {guess}')
            else:
                print('WRONG,I AM ABOUT TO EAT YOU!!\n Try Again')
        no_guesses += 1
    repeat = input("\n\nDO YOU WANT TO PLAY AGAIN(YES OR NO in capital leters)?")


