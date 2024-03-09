import tkinter as tk
from Game import Game


class RockPaperScissorUI(Game):
    def __init__(self, root, game):
        super().__init__(root, "Rock Paper Scissors")
        self.root = root
        self.game = game
        for i, choice in enumerate(game.choices):
            tk.Button(
                root,
                text=choice,
                command=lambda choice=choice: game.play(choice),
                height=3,
                width=6,
            ).grid(row=0, column=i)

        self.result_label = self.create_label("", 1, 1)
        self.score_label = self.create_label("Your Score: 0", 2, 1)
        self.comp_score_label = self.create_label("Computer Score: 0", 3, 1)
