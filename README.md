# ALMOST WORDLE
### Video Demo: 
https://drive.google.com/file/d/19DV7hsmlaQ3L15ZertzGIsBL7eY1LLD9/view?usp=drivesdk
### Description: 

Are you familiar with the New York Times text game *WORDLE*?
Wordle is a text based game where the player has 6 attempts to guess a 5-letters word correctly. This 5-letters word is chosen by the computer.

This is a simple implementation of the popular word guessing game, built using Python. The game is designed to be played in the terminal and allows the user to guess a five-letter word within six attempts. The game provides feedback on each guess, indicating which letters are in the correct position and which letters are present but in the wrong position.

For every guess, the user is presented with a clue of the correct letters in his guesses.

After submitting each guess, the guess is examined and the user is hinted as follows:
- if any letter in the word guessed belongs in the chosen word and is in the right position; the letter changes to GREEN
- if any letter in the word guessed belongs in the chosen word but in the wrong position; the letter changes to YELLOW
- otherwise, the letter does not change at all

### Requirements
Ensure that your machine meets the following requirements:
- Python 3.8+ (preferably Python3.10+)
- A terminal or command prompt window

### Installation
You can install the game by cloning this repository and installing the required packages:
```
git clone https://github.com/me50/farookie007.git
cd farookie007
pip install -r requirements.txt
```

### Usage
To play the game, type and run the following commands in your command line:
```
python project.py
```
The program will ask for input from the user to make a guess.
**Note:** The word list used in this implementation is based on the same one used by Wordle

To run the tests:
```
pytest test_project.py
```

### Design Considerations
A lot of factors were considered in the implementation of this game, some of them are:
- List of words anwers fetched from the internet are stored in a JSON file - `wordle_allowed_answers.json`, in the root folder of the project. This is to reduce dependencies on the internet
- Another list of words which are allowed guesses in the game are stored in a JSON file - `wordle_allowed_guesses.json`, also in the root folder of the project
- The number of attempts allowed before losing the game remain in accordance to the original Wordle game
- If an invalid word is entered, it is handled gracefully rather than causing a crash
- To ensure fairness, a random selection mechanism is implemented for selecting the secret word from the list of words provided
- Note that all entries are case insensitive


### Acknowledgements
This project was inspired by the original Wordle game created by Josh Wardle.
