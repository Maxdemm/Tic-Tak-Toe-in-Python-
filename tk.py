import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.current_player = 'X'

        # Create buttons
        self.buttons = [[None, None, None] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.window, text='', font=('normal', 20), width=8, height=4,
                                              command=lambda row=i, col=j: self.click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def click(self, row, col):
        if self.buttons[row][col]["text"] == '':
            self.buttons[row][col]["text"] = self.current_player
            if self.check_winner(row, col):
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self, row, col):
        # Check row
        if all(self.buttons[row][i]["text"] == self.current_player for i in range(3)):
            return True
        # Check column
        if all(self.buttons[i][col]["text"] == self.current_player for i in range(3)):
            return True
        # Check diagonals
        if all(self.buttons[i][i]["text"] == self.current_player for i in range(3)) or \
                all(self.buttons[i][2 - i]["text"] == self.current_player for i in range(3)):
            return True
        return False

    def check_draw(self):
        return all(self.buttons[i][j]["text"] != '' for i in range(3) for j in range(3))

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ''
        self.current_player = 'X'

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
