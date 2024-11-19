import random
def get_user_choice():
    choices = {1: 'paper', 2: 'scissor', 3: 'rock'}
    choice_num = int(input("Enter your choice (1 for the paper, 2 for the scissor, 3 for  the rock): "))
    return choices.get(choice_num, "Invalid choice")
def get_computer_choice():
    return random.choice(['paper', 'scissor', 'rock'])
def determine_winner(user_choice, computer_choice):
    outcomes = {
        ('Rock', 'Paper'): "Paper covers  the rock! and You lose.",
        ('Rock', 'Scissors'): "Rock smashes the scissors!and You win!",
        ('Paper', 'Rock'): "Paper covers the rock!  and You win!",
        ('Paper', 'Scissors'): "Scissors cuts the paper! and  You lose.",
        ('Scissors', 'Paper'): "Scissors cuts the paper! and You win!",
        ('Scissors', 'Rock'): "Rock smashes the scissors! and You lose."
    }
    if user_choice == computer_choice:
        return "It's a tie!"
    return outcomes.get((user_choice, computer_choice), "It is a tie!")
def play_game():
    print("WELCOME TO THE GAME!!!")
    print("\nenter 1 for the selecting the Rock \n")
    print("\nenter 2 for the  selecting the Paper \n")
    print("\nenter 3 for the selecting the Scissors\n")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You have selected the{user_choice}!")
        print(f"the computer choice is: {computer_choice}\n")
        print("Now it's Time to Play the game")
        print(determine_winner(user_choice, computer_choice)) 
        if input("Do you want to play the game one more time (Yes/No)? ").upper() != 'Y':
            print("Thank you for playing the game!!")
            break

play_game()