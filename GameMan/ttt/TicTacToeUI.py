import tkinter as tk
from ttt.TicTacToe import TicTacToe
from Game import Game


class TicTacToeUI(Game):
    def __init__(self, root, game):
        super().__init__(root, "Tic Tac Toe")
        self.root = root
        self.game = game
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    root,
                    text="",
                    command=lambda i=i, j=j: self.game.play(i, j),
                    height=3,
                    width=6,
                )
                self.buttons[i][j].grid(row=i, column=j)

        self.result_label = self.create_label("", 3, 3)
        self.score_label = self.create_label("Your Score: 0", 4, 3)
        self.comp_score_label = self.create_label("Computer Score: 0", 5, 3)

        self.restart_button = tk.Button(
            root,
            text="Restart",
            command=self.restart_game,
            height=3,
            width=6,
        )
        self.restart_button.grid(row=6, column=3)

    def update_ui(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = self.game.board[i][j]
        self.result_label["text"] = self.game.result
        self.score_label["text"] = f"Your Score: {self.game.score}"
        self.comp_score_label["text"] = f"Computer Score: {self.game.comp_score}"

    def restart_game(self):
        self.game.reset()
        self.update_ui()
