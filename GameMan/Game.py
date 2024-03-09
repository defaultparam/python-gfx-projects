import tkinter as tk


class Game:
    def __init__(self, root, title):
        self.root = root
        self.root.title(title)

    def update_ui(self, result, score, comp_score):
        self.result_label["text"] = result
        self.score_label["text"] = f"Your Score: {score}"
        self.comp_score_label["text"] = f"Computer Score: {comp_score}"

    def create_label(self, text, row, column, columnspan=1):
        label = tk.Label(self.root, text=text)
        label.grid(row=row, column=column, columnspan=columnspan)
        return label
