import random
import time

# Function to display ASCII banner
def show_banner():
    print("""
########################################
#                                      #
#     🎯 WELCOME TO NUMBER GUESSING 🎯  #
#                                      #
########################################
""")

# Function to display main menu
def show_menu():
    print("\n=== Menu ===")
    print("1. Play Game")
    print("2. View High Score")
    print("3. Exit")
    print("-------------------------")

# Function to give hints based on distance from the target
def give_hint(guess, number):
    diff = abs(guess - number)
    if diff > 30:
        print("🔥 You're very far away!")
    elif diff > 15:
        print("🌟 You're far!")
    elif diff > 5:
        print("💡 You're close!")
    else:
        print("✨ Extremely close!")

# Countdown before the game starts
def countdown():
    print("\nGet ready! The game will start in:")
    for i in range(3, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    print("Go! 🎯\n")

# Confetti-style celebration
def celebration():
    confetti = ["✨", "🎉", "🎊", "💥", "🌟"]
    print("\n" + "".join(confetti*5))
    print("CONGRATULATIONS! 🎉 YOU WON! 🎊")
    print("".join(confetti*5) + "\n")

# Function to play the game
def play_game(high_score):
    player_name = input("Enter your name: ").strip() or "Player"
    number_to_guess = random.randint(1, 100)
    attempts = 0
    countdown()
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("❌ Please guess a number between 1 and 100!")
                continue

            if guess < number_to_guess:
                print("⬆ Too Low!")
                give_hint(guess, number_to_guess)
            elif guess > number_to_guess:
                print("⬇ Too High!")
                give_hint(guess, number_to_guess)
            else:
                celebration()
                print(f"🎯 Well done, {player_name}! You guessed it in {attempts} attempts.")
                if high_score is None or attempts < high_score:
                    print("🏆 New High Score!")
                    high_score = attempts
                break
        except ValueError:
            print("❌ Invalid input! Please enter a number.")

    return high_score

# Main function to control game flow
def main():
    high_score = None
    show_banner()
    while True:
        show_menu()
        choice = input("Enter your choice (1-3): ").strip()

        if choice == '1':
            high_score = play_game(high_score)
        elif choice == '2':
            if high_score:
                print(f"🏅 Best score so far: {high_score} attempts")
            else:
                print("No games played yet. No high score!")
        elif choice == '3':
            print("Thanks for playing! Goodbye 👋")
            break
        else:
            print("❌ Invalid choice! Please select from the menu.")

# Start the game
if __name__ == "__main__":
    main()
