import random 


def main():
    while True:
        magicnumber = random.randint(1, 10)
        playerguess = int(input("Let's play a guessing game! Guess a number between 1-10: "))

        print(f"I was thinking of the number {magicnumber}")

        if playerguess == magicnumber:
            print("Are you a mind reader? You win!")
        else:
            print("Sorry, you lose 🥲")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break 

    print("Thanks for playing!")
main()