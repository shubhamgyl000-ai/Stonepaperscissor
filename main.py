import random
# scores
your_score = 0
my_score = 0
# Game Function
def game():
    global your_score, my_score
    Your = input("Enter stone, paper, scissors: ").lower()
    if Your not in ["stone", "paper", "scissors",]:
        print("Invalid choice!")
        return
    My = random.choice(["stone", "paper", "scissors",])
    print("I taken:", My)
    if Your == My:
        print("Result: Tie!")
    elif (Your == "stone" and My == "scissors") or (Your == "paper" and My == "stone") or (Your == "scissors" and My == "paper"):
        print("Result: You Win!")
        your_score += 1
    else:
        print("Result: Me Wins!")
        my_score += 1
    print("Score -> You:", your_score , "| My score:", my_score)
# Main Loop (Menu)
while True:
    print("\n===== STONE PAPER SCISSORS =====")
    print("1. Play Game")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        game()
    elif choice == "2":
        print("Final Score -> You:", your_score, "| My:", my_score)
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
