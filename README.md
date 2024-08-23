
# Rock-Paper-Scissors Game

This is a simple command-line Rock-Paper-Scissors game written in Python. The game allows the user to play against the computer, where the computer randomly picks one of the three options: rock, paper, or scissors. The user can also quit the game at any time.

## How to Play

1. **Run the game**:
   - Execute the Python script in your terminal or command prompt.

2. **Choose an option**:
   - The game will prompt you to choose between "rock", "paper", or "scissors".
   - You can also type "Quit" to terminate the game.

3. **Game logic**:
   - The computer randomly selects "rock", "paper", or "scissors".
   - If your choice matches the computer's, it's a draw.
   - If your choice beats the computer's (e.g., paper beats rock), you win!
   - If the computer's choice beats yours, you lose.
   - If you enter anything other than the valid options, you'll be prompted to try again.

## Features

- **Simple Gameplay**: Just pick "rock", "paper", or "scissors" and see if you can beat the computer.
- **Random Computer Choice**: The computer's choice is random every time you play.
- **Quit Anytime**: You can exit the game by typing "Quit".

## Example Output

```plaintext
|======| RPS - GAME |======|

ROCK    PAPER    SCISSOR

Enter any of the above options, or enter "Quit" to terminate the session
>>> rock
It's a Draw
```

## Technologies Used

- **Python 3.x**: The programming language used to build the game.
- **random module**: Used to randomly select the computer's choice.

## How to Run

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   ```

2. **Run the script**:
   ```bash
   python rps_game.py
   ```

3. **Play the game**:
   - Follow the on-screen prompts to play.

## Future Enhancements

- Add a graphical user interface (GUI) for a more interactive experience.
- Keep track of the user’s score over multiple rounds.
- Provide additional game options, such as a best-of-three mode.
