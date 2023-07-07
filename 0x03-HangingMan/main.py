# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random


def hangman():
    word = random.choice(["superman", "god", "benin", "lion", "animal", "surf", "waves", "spider", "hercules", "zeus",
                          "computer", "middle", "godzilla", "pericles", "europa", "africa", "asia"])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''

    while len(word) > 0:
        main = ""
        missed = 0
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + ""
        if main == word:
            print(main)
            print("You win!")
            break

        print("Guess the word" + main)
        guess = input()
        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess = input()
        if guess not in word:
            turns = turns - 1

        if guess not in word:
            turns -= 1
            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            elif turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            elif turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            elif turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            elif turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            elif turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            elif turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            elif turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            else:
                print("You loose")
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break



def guess():
    name = input("Enter your name")
    print("Welcome" + name)
    print("------------------")
    print('Try to guess the word in less than 18 attempts ')
    hangman()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    guess()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
