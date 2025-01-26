import random
from datetime import datetime
from top_5_players import top_5_users

#Playing the game
def rock_paper_scissors():
    username = input("Enter your username: ").strip()
    options = ["rock", "paper", "scissors"]
    user_score, computer_score = 0, 0

    while user_score < 10 and computer_score < 10:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice not in options:
            print("Invalid choice. Try again.")
            continue
        
        #Computer's choice
        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
        
        #Printing the score
        print(f"Score -> {username}: {user_score}, Computer: {computer_score}")

    #Saving user scores in a txt file
    with open("user_scores.txt", "a") as user_file:
        user_file.write(f"{username},{datetime.now()},{user_score}\n")
    
    #Saving computer scores in a txt file
    with open("computer_scores.txt", "a") as computer_file:
        computer_file.write(f"{username},{datetime.now()},{computer_score}\n")

    print("Game over! Final score recorded.")

#Displaying top 5 users
top_5_users()


def main():
    rock_paper_scissors()

if __name__ == "__main__":
    main()