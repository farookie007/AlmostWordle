import colorama
from project import paint, get_all_words, print_guesses


def test_print_guesses():
    assert print_guesses(["apple", "banana"]) is None


def test_get_all_words():
    word, allowed_answers, allowed_guesses = get_all_words()
    assert isinstance(allowed_answers, list)
    assert isinstance(allowed_guesses, list)
    assert isinstance(word, str)
    assert word in allowed_answers
    all_words = allowed_answers + allowed_guesses
    assert all(map(lambda w: w.isupper(), all_words))
    assert all(map(lambda w: len(w) == 5, all_words))


def test_paint():
    painted_word = paint("abcd")
    assert painted_word.endswith(colorama.Fore.WHITE)
    assert painted_word.startswith(colorama.Fore.WHITE)
    assert "abcd" in painted_word

    # testing for red color
    painted_word = paint("abcd", color="red")
    assert painted_word.endswith(colorama.Fore.WHITE)
    assert painted_word.startswith(colorama.Fore.RED)
    assert "abcd" in painted_word

    # testing for green color
    painted_word = paint("abcd", color="green")
    assert painted_word.endswith(colorama.Fore.WHITE)
    assert painted_word.startswith(colorama.Fore.GREEN)
    assert "abcd" in painted_word

    # testing for yellow color
    painted_word = paint("abcd", color="yellow")
    assert painted_word.endswith(colorama.Fore.WHITE)
    assert painted_word.startswith(colorama.Fore.YELLOW)
    assert "abcd" in painted_word
