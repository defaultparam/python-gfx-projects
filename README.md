# Projects in this repo
- PyTube - Youtube videos downloader
- GameMan - Includes games like rock paper scissor and tic tac toe (more to come soon)
- PyCalcy - Yet another calculator app built with tkinter
- PyConverter - A simple feet to meter converter, I built to test modules in Tkinter. (Ignore this one lol)

## PyTube
- It is a YT video downloader whose primary function is to download YT videos for offline viewing. (It uses an already made package named PyTube, and is more of a custom port for minimal functionality)
- The application provides a simple graphical user interface (GUI) built with Tkinter.
- The application includes a progress bar and a percentage label that update in real time to show the progress of the video download.
- The application handles errors gracefully. If a video is age-restricted, the download is cancelled and an appropriate message is displayed.
- The application automatically selects the highest resolution stream available for download.
- Once the download is complete, a completion message is displayed to the user.

## GameMan
- GameMan currently supports two games: Tic Tac Toe and Rock Paper Scissors. Each game is implemented as a separate class with its own logic and user interface.
- With project I learnt how to separate the presentation layer from the logic used inside the code. Letting me aim towards working on "the clean-architecture principle"
- For TicTacToe:
    - It is a Player v Computer mode of the game
    - Presents you with a 3x3 grid, player always starts first
    - Win check for row column and diagonal on each move
    - Score is updated on invdividual wins
    - Option to reset the game board.
- For rock paper scissor,
    - It is also a Player v Computer mode of the game
    - Gives you buttons and computer plays on random.
    - Score is updated after each win
    - Abstracted using a common Game to be shared amongst other GameMan projects.

## Calculator app
- It is a simple GUI based app built with tkinter to let user perform mathematical operations supporting add, subtract, multiply, divide.

### Other ideas to be implemented
- HangMan game! - Add sounds!
