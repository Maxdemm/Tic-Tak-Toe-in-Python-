import tkinter as tk
from tkinter import messagebox
from logic import Game

class App:
    def __init__(self, master):
        self.master = master
        master.title("tic-tak-toe_bat1")

        self.game = Game()

        self.buttons = []
        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = tk.Button(master, text="", font=("Helvetica", 24), width=7, height=3,
                                   command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j, padx=2, pady=2)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

        self.play_again_button = tk.Button(master, text="Почати спочатку", command=self.reset_game)
        self.play_again_button.grid(row=3, column=0, columnspan=3, pady=10)

        self.score_label = tk.Label(master, text="")
        self.score_label.grid(row=4, column=0, columnspan=3, pady=10)

    def on_button_click(self, row, col):
        if self.game.is_valid_move(row, col):
            symbol = 'X' if self.game.step_number % 2 == 0 else 'O'
            self.game.field[row][col] = symbol
            self.buttons[row][col].config(text=symbol, state=tk.DISABLED)
            self.game.step_number += 1

            result = self.game.check_winning_conditions()
            if result:
                self.display_winner(result)
            elif not self.game.has_steps():
                self.display_draw()

    def display_winner(self, winner):
        messagebox.showinfo("Гра закінчена", f"Переможець: {winner}")
        self.update_score()
        self.reset_game()

    def display_draw(self):
        messagebox.showinfo("Гра закінчена", "Нічия")
        self.update_score()
        self.reset_game()

    def reset_game(self):
        self.game = Game()
        for row in self.buttons:
            for button in row:
                button.config(text="", state=tk.NORMAL)
        self.play_again_button.config(state=tk.NORMAL)

    def update_score(self):
        score_text = f"Рахунок: X - {self.game.score['X']}, O - {self.game.score['O']}"
        self.score_label.config(text=score_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

