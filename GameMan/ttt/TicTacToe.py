from random import choice


class TicTacToe:
    def __init__(self, ui):
        self.ui = ui
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.score = 0
        self.comp_score = 0
        self.result = ""

    def play(self, i, j):
        if self.board[i][j] == "" and not self.result:
            self.board[i][j] = self.current_player
            if self.check_win(self.current_player):
                self.result = f"{self.current_player} wins!"
                self.update_score()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":
                    self.computer_play()
            self.ui.update_ui()

    def check_win(self, player):
        return (
            any(all(cell == player for cell in row) for row in self.board)
            or any(all(row[i] == player for row in self.board) for i in range(3))
            or all(self.board[i][i] == player for i in range(3))
            or all(self.board[i][2 - i] == player for i in range(3))
        )

    def computer_play(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    self.board[i][j] = self.current_player
                    if self.check_win(self.current_player):
                        self.result = f"{self.current_player} wins!"
                        self.update_score()
                    else:
                        self.current_player = "X"
                    return

    def update_score(self):
        if self.result == "X wins!":
            self.score += 1
        elif self.result == "O wins!":
            self.comp_score += 1

    def reset(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.result = ""
