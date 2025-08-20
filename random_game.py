import tkinter as tk
from tkinter import messagebox
import random

class GuessGameUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Number Guessing Game")
        self.resizable(False, False)
        self.number = random.randint(1, 50)
        self.current_player = None
        self.player1 = None
        self.player2 = None
        
        self._build_name_entry()

    def _build_name_entry(self):
        # Frame to gather player names
        frame = tk.Frame(self, padx=20, pady=20)
        frame.pack()
        
        tk.Label(frame, text="Player 1 Name:", font=(None, 12)).grid(row=0, column=0, sticky="e", pady=5)
        self.name1_entry = tk.Entry(frame, font=(None, 12))
        self.name1_entry.grid(row=0, column=1, pady=5)
        
        tk.Label(frame, text="Player 2 Name:", font=(None, 12)).grid(row=1, column=0, sticky="e", pady=5)
        self.name2_entry = tk.Entry(frame, font=(None, 12))
        self.name2_entry.grid(row=1, column=1, pady=5)
        
        start_btn = tk.Button(frame, text="Start Game", font=(None, 12, 'bold'),
                              command=self._start_game)
        start_btn.grid(row=2, columnspan=2, pady=10)

    def _start_game(self):
        p1 = self.name1_entry.get().strip()
        p2 = self.name2_entry.get().strip()
        if not p1 or not p2:
            messagebox.showwarning("Missing Names", "Please enter names for both players.")
            return
        self.player1, self.player2 = p1, p2
        self.current_player = self.player1
        # Clear window and build game UI
        for widget in self.winfo_children():
            widget.destroy()
        self._build_game_ui()

    def _build_game_ui(self):
        frame = tk.Frame(self, padx=20, pady=20)
        frame.pack()
        
        self.turn_label = tk.Label(frame, text=f"{self.current_player}'s turn", font=(None, 14))
        self.turn_label.pack(pady=(0,10))
        
        guess_frame = tk.Frame(frame)
        guess_frame.pack()
        tk.Label(guess_frame, text="Your Guess:", font=(None, 12)).grid(row=0, column=0, padx=(0,10))
        self.guess_entry = tk.Entry(guess_frame, font=(None, 12), width=5)
        self.guess_entry.grid(row=0, column=1)
        self.guess_entry.focus()
        
        submit_btn = tk.Button(frame, text="Submit", font=(None, 12, 'bold'),
                               command=self._check_guess)
        submit_btn.pack(pady=10)
        
        self.feedback_label = tk.Label(frame, text="", font=(None, 12))
        self.feedback_label.pack()

    def _check_guess(self):
        try:
            guess = int(self.guess_entry.get())
        except ValueError:
            self.feedback_label.config(text="Please enter a valid integer.")
            return
        
        if guess > self.number:
            self.feedback_label.config(text="Too high. Try a smaller number.")
        elif guess < self.number:
            self.feedback_label.config(text="Too low. Try a larger number.")
        else:
            messagebox.showinfo("Congratulations!", f"{self.current_player} wins! The number was {self.number}.")
            self.destroy()
            return
        
        # Switch turn
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1
        self.turn_label.config(text=f"{self.current_player}'s turn")
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.focus()

if __name__ == "__main__":
    app = GuessGameUI()
    app.mainloop()
