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
    while not isinstance(word_length, int):  # Tests the users input to see if it is a valid word length
        if word_length == "4" or word_length == "four":
            word_length = 4
        elif word_length == "5" or word_length == "five":
            word_length = 5
        elif word_length == "6" or word_length == "six":
            word_length = 6
        elif word_length == "7" or word_length == "seven":
            word_length = 7
        else:
            print("Please pick a number that is between 4 and 7!\n")  # If the input isn't a valid word length asks user to resubmit
            word_length = input("Word length:\n").strip().lower()
    print(f"You have choosen a {word_length} letter word.\n")
    return word_length


def get_word(length):
    """
    Generates a random number and uses that to
    get a random word from the worldlist.txt text file.
    File contains 500 words of each length.
    """
    length_coefficent = (length - 4) * 500  # Var to point to correct group of 500 words
    wordlist = open('wordlist.txt', 'r').readlines()
    word = wordlist[random.randrange(500) + length_coefficent]  # Picks a random line to copy in the correct word length group
    open('wordlist.txt', 'r').close()
    letters_list = [letter for letter in word if letter.isalpha()]  # Turns the chosen word into a list of letters
    return letters_list


def check_guess(guess):
    """
    Checks the players guess against the mystery word.
    """
    global REMAINING_GUESSES
    global GUESSES
    global REVEALED_LETTERS
    while (len(guess) > 1 or not guess.isalpha()) or guess in GUESSES:  # Tests if the guess is a valid letter
        if guess in GUESSES:
            print(f"You've already guessed {guess}!")
        else:
            print("Please enter one letter!")
        guess = input("Guess a letter:\n").lower()
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
                REVEALED_LETTERS[ind] = guess  # Replaces the correct * in the word display with the guessed letter


def play_game():
    """
    Main function that runs the game.
    """
    global MYSTERY_WORD
    global REMAINING_GUESSES
    global GUESSES
    global REVEALED_LETTERS
    print("Guess letters to find the word before you run out of attempts!")
    MYSTERY_WORD = [letter for letter in get_word(get_word_length())] 
    for letter in MYSTERY_WORD:
        REVEALED_LETTERS.append("*")
    print("------------------------------------\n")
    print(f"Guesses remaining: {REMAINING_GUESSES}\n")
    while REMAINING_GUESSES > 0:  # Loops while user has guesses left
        if GUESSES:  # Displays previous guesses if there are any
            if "*" not in REVEALED_LETTERS:
                print("Congratulations, you win!")
                return
            print(f"Letters guessed: {', '.join(GUESSES)}\n")
            print(f"Correct letters: {''.join(REVEALED_LETTERS)}\n")
        check_guess(input("Guess a letter:\n").lower())  # Checks the users guess against the mystery word
    if REMAINING_GUESSES == 0:
        print("Better luck next time!")
        print(f"The word was:{''.join(MYSTERY_WORD)}")  # Displays word for user


def reset():
    """
    Resets the game and asks the user if they would like to play again.
    """
    global MYSTERY_WORD
    global REMAINING_GUESSES
    global GUESSES
    global REVEALED_LETTERS
    global PLAY_AGAIN
    MYSTERY_WORD = []
    REMAINING_GUESSES = 5
    GUESSES = []
    REVEALED_LETTERS = []
    PLAY_AGAIN = True
    replay = ""
    while not isinstance(replay, bool):
        replay = input("Would you like to play again?\n").lower()
        if replay == "yes" or replay == "y":
            replay = True
        elif replay == "no" or replay == "n":
            PLAY_AGAIN = False
            replay = False
        else:
            print("Please choose 'yes' or 'no'")
    print("------------------------------------\n")


print("Welcome!")
while PLAY_AGAIN:
    play_game()
    reset()
print("Thanks for playing.")
