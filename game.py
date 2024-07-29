import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(user_choice):
    global user_score, computer_score

    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1
    
    update_scores()
    result_message = f"You chose {user_choice}, computer chose {computer_choice}. {result}"
    messagebox.showinfo("Result", result_message)

# Function to handle button click
def on_button_click(choice):
    determine_winner(choice)

# Function to update the score labels
def update_scores():
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    update_scores()

# Initialize scores
user_score = 0
computer_score = 0

# Setting up the GUI
root = tk.Tk()
root.title("Rock Paper Scissors")

# Creating labels to display scores
user_score_label = tk.Label(root, text=f"Your Score: {user_score}", font=('Helvetica', 14))
user_score_label.pack(pady=10)

computer_score_label = tk.Label(root, text=f"Computer Score: {computer_score}", font=('Helvetica', 14))
computer_score_label.pack(pady=10)

# Creating buttons for user choices
rock_button = tk.Button(root, text="Rock", font=('Helvetica', 14), command=lambda: on_button_click('rock'))
rock_button.pack(pady=10)

paper_button = tk.Button(root, text="Paper", font=('Helvetica', 14), command=lambda: on_button_click('paper'))
paper_button.pack(pady=10)

scissors_button = tk.Button(root, text="Scissors", font=('Helvetica', 14), command=lambda: on_button_click('scissors'))
scissors_button.pack(pady=10)

# Creating a reset button
reset_button = tk.Button(root, text="Reset", font=('Helvetica', 14), command=reset_game)
reset_button.pack(pady=10)

# Running the GUI
root.mainloop()