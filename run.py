import random
MYSTERY_WORD = []
REMAINING_GUESSES = 5
GUESSES = []
REVEALED_LETTERS = []
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
    """
    Checks the players guess against the mystery word.
    """
    global REMAINING_GUESSES
    global GUESSES
    global REVEALED_LETTERS
    while (len(guess) > 1 or not guess.isalpha()) or guess in GUESSES:
        if guess in GUESSES:
            print(f"You've already guessed {guess}!")
        else:
            print("Please enter one letter!")
        guess = input("Guess a letter:").lower()
    GUESSES.append(guess)
    if guess not in MYSTERY_WORD:
        print(f"Sorry, {guess} isn't correct!")
        print("------------------------------------\n")
        REMAINING_GUESSES = REMAINING_GUESSES - 1
        print(f"Guesses remaining: {REMAINING_GUESSES}\n")
        return
    if guess in MYSTERY_WORD:
        for ind in range(len(MYSTERY_WORD)):
            if MYSTERY_WORD[ind] == guess:
                REVEALED_LETTERS[ind] = guess


def play_game():
    """
    Main function that runs the game.
    """
    global MYSTERY_WORD
    global REMAINING_GUESSES
    global GUESSES
    global REVEALED_LETTERS
    MYSTERY_WORD = []
    REMAINING_GUESSES = 5
    GUESSES = []
    print("Guess letters to find the word before you run out of attempts!")
    MYSTERY_WORD = [letter for letter in get_word(get_word_length())]
    for letter in MYSTERY_WORD:
        REVEALED_LETTERS.append("*")
    print("------------------------------------\n")
    print(f"Guesses remaining: {REMAINING_GUESSES}\n")
    while REMAINING_GUESSES > 0:
        if GUESSES:
            if "*" not in REVEALED_LETTERS:
                print("Congratulations, you win!")
                return
            print(f"Letters guessed: {', '.join(GUESSES)}\n")
            print(f"Correct letters: {''.join(REVEALED_LETTERS)}\n")
        check_guess(input("Guess a letter:\n").lower())
    if REMAINING_GUESSES == 0:
        print("Better luck next time!")
        print(f"The word was:{''.join(MYSTERY_WORD)}")


def reset():
    print("This will reset everything ready to play again")


print("Welcome!")
while PLAY_AGAIN:
    play_game()
    reset()
print("Thanks for playing.")