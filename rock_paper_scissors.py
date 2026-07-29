import random

def show_menu():
    print("\n=== ROCK, PAPER, SCISSORS + WELL ===")
    print("1. Play a round")
    print("2. Show current score")
    print("3. Game rules")
    print("0. Exit")

def get_menu_choice():
    while True:
        choice = input("Choose an option: ").strip()
        if choice in ["1", "2", "3", "0"]:
            return int(choice)
        print("Error! Please enter a number from 0 to 3.")

def show_rules():
    print("\n--- GAME RULES ---")
    print("• Rock beats Scissors (blunts them).")
    print("• Scissors beat Paper (cuts it).")
    print("• Paper beats Rock and Well (covers them).")
    print("• Well beats Rock and Scissors (they drown in it).")
    print("The game continues until you choose to exit via the menu.")

def get_user_choice():
    print("\nYour turn:")
    print("1. Rock")
    print("2. Scissors")
    print("3. Paper")
    print("4. Well")
    while True:
        choice = input("Select your option (1-4): ").strip()
        if choice in ["1", "2", "3", "4"]:
            options = {1: "Rock", 2: "Scissors", 3: "Paper", 4: "Well"}
            return options[int(choice)]
        print("Error! Please enter 1, 2, 3, or 4.")

def determine_winner(user, computer):
    if user == computer:
        return "draw"
    
    winning_rules = {
        "Rock": ["Scissors"],
        "Scissors": ["Paper"],
        "Paper": ["Rock", "Well"],
        "Well": ["Rock", "Scissors"]
    }
    
    if computer in winning_rules[user]:
        return "user"
    else:
        return "computer"

def play_round(score):
    choices = ["Rock", "Scissors", "Paper", "Well"]
    user_move = get_user_choice()
    computer_move = random.choice(choices)
    
    print(f"\nYou chose: {user_move}")
    print(f"Computer chose: {computer_move}")
    
    result = determine_winner(user_move, computer_move)
    
    if result == "draw":
        print("It's a tie in this round!")
        score["draws"] += 1
    elif result == "user":
        print("You won this round!")
        score["user"] += 1
    else:
        print("Computer won this round.")
        score["computer"] += 1

def show_score(score):
    print("\n=== CURRENT SCORE ===")
    print(f"Player: {score['user']}")
    print(f"Computer: {score['computer']}")
    print(f"Draws: {score['draws']}")

def main():
    game_score = {"user": 0, "computer": 0, "draws": 0}
    
    while True:
        show_menu()
        choice = get_menu_choice()
        
        if choice == 1:
            play_round(game_score)
        elif choice == 2:
            show_score(game_score)
        elif choice == 3:
            show_rules()
        elif choice == 0:
            print("\nThank you for playing! See you next time.")
            show_score(game_score)
            break

if __name__ == "__main__":
    main()

