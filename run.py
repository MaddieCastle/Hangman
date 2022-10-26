import random
MYSTERY_WORD = []
REMAINING_GUESSES = 5
GUESSES = []
PLAY_AGAIN = True


def get_word_length():
    """
    Asks user to pick word length and prints it to the terminal.
    """
    print("Choose the word length, between 4 and 7 letters long.\n")
    word_length = input("Word length:\n").strip().lower()
    while not isinstance(word_length, int):
        if word_length == "4" or word_length == "four":
            word_length = 4
        elif word_length == "5" or word_length == "five":
            word_length = 5
        elif word_length == "6" or word_length == "six":
            word_length = 6
        elif word_length == "7" or word_length == "seven":
            word_length = 7
        else:
            print("Please pick a number that is between 4 and 7!\n")
            word_length = input("Word length:\n").strip().lower()

    print(f"You have choosen a {word_length} letter word.\n")
    return word_length


def get_word(length):
    """
    Generates a random number and uses that to
    get a random word from the worldlist.txt text file.
    """
    length_coefficent = (length - 4) * 500
    wordlist = open('wordlist.txt', 'r').readlines()
    word = wordlist[random.randrange(500) + length_coefficent]
    open('wordlist.txt', 'r').close()
    letters_list = [letter for letter in word if letter.isalpha()]
    return letters_list


def check_guess(guess):
    print("This will check if the guessed letter is in the mystery word.")


def play_game():
    print("this will be the main function that runs the game")
    global MYSTERY_WORD
    MYSTERY_WORD = [letter for letter in get_word(get_word_length())]
    print(MYSTERY_WORD)


def reset():
    print("This will reset everything ready to play again")


print("Welcome!")
while PLAY_AGAIN:
    play_game()
    reset()
print("Thanks for playing.")