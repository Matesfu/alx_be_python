import random

while True:
    random_number= random.randint(1,10)
    title= "I'm thinking a number between 1 and 10, can you guess it?"
    i= True
    while i:
        guess= int(input(title))
        title= "guess: "
        match guess:
            case _ if guess == random_number:
                print("Congratulations, you guessed it!")
                i= False
            case _ if guess > random_number:
                print("Oops, it is higher, Give it another shot!")
            case _ if guess < random_number:
                print("nope, your guess is a bit low, Give it another shot!")
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        print("...(new game started)")
    elif play_again != "yes":
        print("Thanks for playing! 👋")
        break


