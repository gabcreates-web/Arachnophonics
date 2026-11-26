import time 

def check_word(correct, incorrect, word, tries):
    guess = input("Guess a letter: ").upper()

    if guess in word:
        if guess not in correct:
            correct.append(guess)
            print("Correct guess!")
        else:
            print("You already guessed that letter!")

    elif guess in incorrect:
        print("You already guessed that letter!")

    else:
        incorrect.append(guess)
        tries += 1
        print("Wrong guess!")

    return tries

def clear_screen():
    print("\n" * 50)

def load_words(path):
    """Return a list of words read from `path` (one per line)."""
    # Provided helper — call this from main.py in L15.
    with open(path) as f:
        return [line.strip() for line in f if line.strip()]


def build_display(word, correct):
    """Return the word with unguessed letters replaced by '_'."""
    # Provided helper — call this from main.py in L15.
    return " ".join(c if c in correct else "_" for c in word)

def introduction(name):
    print("==============================")
    print(f" Welcome to ArachnoPhonics, {name}!")
    print("==============================")
