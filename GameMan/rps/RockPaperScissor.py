import random


class RockPaperScissor:
    def __init__(self, ui):
        self.ui = ui
        self.choices = ["Rock", "Paper", "Scissors"]
        self.score = 0
        self.comp_score = 0
        self.result = ""

    def play(self, player_choice):
        computer_choice = random.choice(self.choices)
        if player_choice == computer_choice:
            self.result = f"It's a tie! {computer_choice} was chosen by the computer."
        elif (
            (player_choice == "Rock" and computer_choice == "Scissors")
            or (player_choice == "Scissors" and computer_choice == "Paper")
            or (player_choice == "Paper" and computer_choice == "Rock")
        ):
            self.result = f"You win! {computer_choice} was chosen by the computer."
            self.score += 1
        else:
            self.result = f"Computer wins! {computer_choice} was chosen by the computer."
            self.comp_score += 1
        self.ui.update_ui(self.result, self.score, self.comp_score)
