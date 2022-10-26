MYSTERY_WORD = []
REMAINING_GUESSES = 5
GUESSES = []
PLAY_AGAIN = True


def get_word_length():
    print("This will ask the player to choose the word length")


def get_word():
    print("This will get a word of the chosen length")


def check_guess(guess):
    print("This will check if the guessed letter is in the mystery word.")


def play_game():
    print("this will be the main function that runs the game")


def reset():
    print("This will reset everything ready to play again")


print("Welcome!")
while PLAY_AGAIN:
    play_game()
    reset()
print("Thanks for playing.")