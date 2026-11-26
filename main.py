import spiderDraw as sd
import random
import time
from functions import load_words, build_display, check_word, clear_screen, introduction

SPIDER_STAGES = [
    sd.spider_0,
    sd.spider_1,
    sd.spider_2,
    sd.spider_3,
    sd.spider_4,
    sd.spider_5,
    sd.spider_6
]

MAX_WRONG = 6


def play_round():
    introduction(input("Your name: "))

    words = load_words("words.txt")
    word = random.choice(words).upper()

    correct = []
    incorrect = []

    tries = 0
    game = True

    while game:
        print(SPIDER_STAGES[tries]())

        progress = build_display(word, correct)
        print(progress)

        print("Incorrect guesses:", incorrect)

        tries = check_word(correct, incorrect, word, tries)

        progress = build_display(word, correct)

        if "_" not in progress:
            print("Congratulations! You win!")
            game = False

        if tries >= MAX_WRONG:
            print("Game over! You lose!")
            game = False

        if game:
            clear_screen()
            time.sleep(1)

    print("The word was:", word)


def main():
    play_again = "yes"

    while play_again.lower() == "yes":
        play_round()
        play_again = input("Would you like to play again? (yes/no): ")

    print("Thanks for playing ArachnoPhonics!")


if __name__ == "__main__":
    main()
