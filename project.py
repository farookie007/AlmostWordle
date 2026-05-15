import time
import colorama
import json
import random
import tabulate as tb
from pyfiglet import Figlet


def main():
    colorama.init()

    # Display the title of the game
    menu()

    word, allowed_answers, allowed_guesses = get_all_words()
    word_index = list(word)
    LIVES = 6
    trials = 0
    guess_list = [["∙"] * 5] * LIVES  # for storing the user's guess
    # print the empty `WORDLE` table format
    print_guesses(guess_list)
    while LIVES > 0:
        # Taking user's guess
        guess = input("\nEnter your guess: ").strip().upper()

        # Checking if the guess is a valid word, otherwise, reprompt the user
        if len(guess) != 5:
            print(paint("Error:", "red"), "Your answer must be a five letters word\n")
            time.sleep(0.5)
            print_guesses(guess_list)
            continue

        # If the value entered is not a valid word or is not allowed
        if guess not in allowed_answers and guess not in allowed_guesses:
            print(paint("Error:", "red"), f'"{guess}" not in words list\n')
            time.sleep(0.5)
            print_guesses(guess_list)
            continue

        # For storing the guess word with their corresponding pigment
        colored_guess_word = list()

        # Checking letters in the correct position
        for i, letter in enumerate(guess, start=0):
            if letter == word_index[i]:  # correct letter and in the right position
                letter = paint(letter, "green")
            elif letter in word:  # correct letter but in the wrong position
                letter = paint(letter, "yellow")
            else:  # wrong letter
                letter = paint(letter)
            colored_guess_word.append(letter)

        # Checking if the word has already been guessed by the user
        if colored_guess_word in guess_list:
            print(paint("WARNING:", "yellow"), f"You have already guessed {guess}")
            time.sleep(0.5)
            print_guesses(guess_list)
            continue

        # Adding the pigmented guessed word the to the `guess_list`
        guess_list[trials] = colored_guess_word
        print_guesses(guess_list)

        # Decrementing the number of trials left
        LIVES -= 1
        trials += 1

        # lives_remaining = f"{'🟢' * trials}{'🔴' * (5-trials)}"    # commented out because some machine does not have support for emojis
        lives_remaining = f"{paint('●', color='green') * LIVES}               {paint('●', color='red') * trials}"
        print(lives_remaining, "\n")

        if guess == word:
            print("Welldone!!", end=" ")
            break

    print(f"The answer is {word}")
    print_guesses([[paint(w, "green") for w in word]], animated=True)
    time.sleep(1)


def menu():
    fig = Figlet()
    animate(fig.renderText("W o r d l e ! !".upper()), type_delay=0.001)


def animate(*sentences, end=" ", type_delay=0.01):
    time.sleep(type_delay)
    for sentence in sentences:
        for char in sentence:
            print(char, end="", flush=True)
            time.sleep(type_delay)
        print(end, end="")
    print()  # to ensure that it is ended with a newline


def print_guesses(guess_list, animated=False):
    """
    Function to print all the guesses in the guesses list

    Params:
        :guess_list (List[List]): a list of list containing the guesses by the player.
                                 this list is fit for the `tb.tabulate` function
    Return:
        :None
    """
    tabular_data = tb.tabulate(guess_list, tablefmt="grid")
    if animated:
        tabular_data = tabular_data.split("\n")
        for i, line in enumerate(tabular_data, start=1):
            if i % 2 == 0:
                animate(line)
            else:
                print(line)
        return
    print(tabular_data)


def paint(text: str, color: str = "white"):
    """returns the text in a specified color and resets the color after printing"""
    return (
        colorama.Fore.__dict__.get(color.upper(), "WHITE") + text + colorama.Fore.WHITE
    )


def get_all_words():
    """Returns a tuple of a five letters word and all five letters words possibilities."""
    with open("wordle_allowed_guesses.json", "r") as fp:
        allowed_guesses = json.load(fp)
    with open("wordle_allowed_answers.json", "r") as fp:
        allowed_answers = json.load(fp)
    word = random.choice(allowed_answers)
    return word, allowed_answers, allowed_guesses


if __name__ == "__main__":
    main()
