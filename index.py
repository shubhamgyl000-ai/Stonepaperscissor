import random
import tkinter as tk

# scores (same as your code)
your_score = 0
my_score = 0

# Game Function (your logic, slightly adapted for GUI)
def game(user_choice):
    global your_score, my_score

    Your = user_choice
    My = random.choice(["stone", "paper", "scissors"])

    result = "I taken: " + My + "\n"

    if Your == My:
        result += "Result: Tie!"
    elif (Your == "stone" and My == "scissors") or \
         (Your == "paper" and My == "stone") or \
         (Your == "scissors" and My == "paper"):
        result += "Result: You Win!"
        your_score += 1
    else:
        result += "Result: Me Wins!"
        my_score += 1

    result_label.config(text=result)
    score_label.config(text=f"Score -> You: {your_score} | My: {my_score}")


# Reset Function
def reset_score():
    global your_score, my_score
    your_score = 0
    my_score = 0
    score_label.config(text="Score -> You: 0 | My: 0")
    result_label.config(text="Score Reset!")


# Exit Function
def exit_game():
    root.destroy()


# GUI Window
root = tk.Tk()
root.title("STONE PAPER SCISSORS")
root.geometry("350x350")

# Title
title = tk.Label(root, text="STONE PAPER SCISSORS", font=("Arial", 16))
title.pack(pady=10)

# Buttons (instead of input)
btn_stone = tk.Button(root, text="Stone", width=15, command=lambda: game("stone"))
btn_stone.pack(pady=5)

btn_paper = tk.Button(root, text="Paper", width=15, command=lambda: game("paper"))
btn_paper.pack(pady=5)

btn_scissors = tk.Button(root, text="Scissors", width=15, command=lambda: game("scissors"))
btn_scissors.pack(pady=5)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Score Display
score_label = tk.Label(root, text="Score -> You: 0 | My: 0", font=("Arial", 12))
score_label.pack(pady=5)

# Extra Buttons
reset_btn = tk.Button(root, text="Reset Score", command=reset_score)
reset_btn.pack(pady=5)

exit_btn = tk.Button(root, text="Exit", command=exit_game)
exit_btn.pack(pady=5)

# Run App
root.mainloop()
