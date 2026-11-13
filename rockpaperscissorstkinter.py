
import tkinter as tk
import random

# Main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("600x550")
root.configure(bg="#20243a")
root.resizable(False, False)

# Score variables
player_score = 0
computer_score = 0
draw_score = 0

# Choices
choices = ["Rock", "Paper", "Scissors"]

emojis = {
    "Rock": "✊",
    "Paper": "✋",
    "Scissors": "✌"
}

# Game function
def play(user_choice):
    global player_score, computer_score, draw_score

    computer_choice = random.choice(choices)

    user_label.config(
        text=f"You: {emojis[user_choice]} {user_choice}"
    )

    computer_label.config(
        text=f"Computer: {emojis[computer_choice]} {computer_choice}"
    )

    if user_choice == computer_choice:
        result_label.config(
            text="🤝 IT'S A DRAW!",
            fg="#ffc107"
        )
        draw_score += 1

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or
        (user_choice == "Paper" and computer_choice == "Rock")
        or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result_label.config(
            text="🎉 YOU WIN!",
            fg="#00e676"
        )
        player_score += 1

    else:
        result_label.config(
            text="😢 COMPUTER WINS!",
            fg="#ff5252"
        )
        computer_score += 1

    update_score()


# Update scoreboard
def update_score():
    score_label.config(
        text=f"YOU: {player_score}     "
             f"DRAWS: {draw_score}     "
             f"COMPUTER: {computer_score}"
    )


# Restart game
def restart():
    global player_score, computer_score, draw_score

    player_score = 0
    computer_score = 0
    draw_score = 0

    user_label.config(text="You: Waiting...")
    computer_label.config(text="Computer: Waiting...")
    result_label.config(text="Choose your move!", fg="white")

    update_score()


# Heading
title = tk.Label(
    root,
    text="✊ ROCK PAPER SCISSORS ✌",
    font=("Arial", 23, "bold"),
    bg="#20243a",
    fg="white"
)
title.pack(pady=25)

# Instructions
instruction = tk.Label(
    root,
    text="Choose your weapon!",
    font=("Arial", 16),
    bg="#20243a",
    fg="#bbbbbb"
)
instruction.pack(pady=10)

# Choice buttons
button_frame = tk.Frame(root, bg="#20243a")
button_frame.pack(pady=25)

tk.Button(
    button_frame,
    text="✊\nROCK",
    font=("Arial", 16, "bold"),
    width=10,
    height=3,
    bg="#3498db",
    fg="white",
    command=lambda: play("Rock")
).grid(row=0, column=0, padx=8)

tk.Button(
    button_frame,
    text="✋\nPAPER",
    font=("Arial", 16, "bold"),
    width=10,
    height=3,
    bg="#9b59b6",
    fg="white",
    command=lambda: play("Paper")
).grid(row=0, column=1, padx=8)

tk.Button(
    button_frame,
    text="✌\nSCISSORS",
    font=("Arial", 16, "bold"),
    width=10,
    height=3,
    bg="#e67e22",
    fg="white",
    command=lambda: play("Scissors")
).grid(row=0, column=2, padx=8)

# Player and computer choices
user_label = tk.Label(
    root,
    text="You: Waiting...",
    font=("Arial", 16, "bold"),
    bg="#20243a",
    fg="white"
)
user_label.pack(pady=10)

computer_label = tk.Label(
    root,
    text="Computer: Waiting...",
    font=("Arial", 16, "bold"),
    bg="#20243a",
    fg="white"
)
computer_label.pack(pady=10)

# Result
result_label = tk.Label(
    root,
    text="Choose your move!",
    font=("Arial", 22, "bold"),
    bg="#20243a",
    fg="white"
)
result_label.pack(pady=20)

# Scoreboard
score_label = tk.Label(
    root,
    text="YOU: 0     DRAWS: 0     COMPUTER: 0",
    font=("Arial", 14, "bold"),
    bg="#303650",
    fg="#00e5ff",
    padx=15,
    pady=15
)
score_label.pack(pady=10)

# Restart button
restart_button = tk.Button(
    root,
    text="🔄 RESTART GAME",
    font=("Arial", 13, "bold"),
    bg="#27ae60",
    fg="white",
    width=20,
    command=restart
)
restart_button.pack(pady=15)

# Run game
root.mainloop()
