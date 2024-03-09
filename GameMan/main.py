import tkinter as tk
from ttt.TicTacToeUI import TicTacToeUI
from ttt.TicTacToe import TicTacToe
from rps.RockPaperScissor import RockPaperScissor
from rps.RockPaperScissorUI import RockPaperScissorUI

root = tk.Tk()
root.geometry("500x500")


# Implement argparse to select game before launching GameMan
# game = RockPaperScissor(None)
# ui = RockPaperScissorUI(root, game)
game = TicTacToe(None)
ui = TicTacToeUI(root, game)
game.ui = ui
root.mainloop()
