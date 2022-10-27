# Hangman
Hangman is a game about guessing letters to reveal a mystery word.

It runs on Python code in the Code Institute mock terminal on Heroku.

It is live [here.](https://hangmanmc.herokuapp.com/)
![Image of the game displayed on https://ui.dev/amiresponsive](/images/responsive.jpg)
## How to play
The player chooses the length of the mystery word.

The mystery word is displayed a number of *'s.

The player guesses letters that they think might be in the mystery word.

Incorrect guesses causes the remaining guesses counter to decrease.

Correct guesses replace the corresponding * in the mystery word with the guessed letter.

The player wins by guessing all the letters before the remaining guesses counter hits 0.

## Features
- Word length chosen by user, between 4 and 7 letters long.

![Image of word length input screen](/images/wordlength.jpg)
- Random word of chosen length picked from 500 words of each length.
- Display number of guesses remaining.
- Display letters already guessed.

![Image of guesses remaining and letters guessed display](/images/guessesremaining.jpg)
- Reveals word if user runs out of guesses.

![Showing the revealed word if user runs out of guesses](/images/revealedword.jpg)
- Input validation
  - Choosing the word length requires a number between 4 and 7.
  - Guesses require a single alphabetic character.
  - Previously guessed letters can't be guessed again.
  - Invalid values display a message and prompt resubmission.

![image showing resubmission prompt](/images/letterguessed.jpg)

## Testing
I have tested the code via:
- A PEP8 linter
- Inputting invalid inputs
- In my local terminal

All methods returned no problems.

## Bugs
### Solved Bugs
- When writing the code for revealing a letter that has been guessed correctly, only the first instance of that letter was being revealed. I fixed this by changing `MYSTERY_WORD` to a list of letters instead of a string. This allowed me to iterate through it and replace every instance of a letter.
### Remaining Bugs
No bugs remain.

## Deployment
This game is deployed in Code institute's mock terminal for Heroku [here.](https://hangmanmc.herokuapp.com/) The steps to deploy were as follows:
1. Create a Heroku app
2. Set a config var with key: PORT and value: 8000
3. Set buildbacks to Python and then NodeJS
4. Link the app to the GitHub repository
5. Click on enable automatic deploys

## Credits
- Code institute for the mock terminal
- [The Free Dictionary](https://www.thefreedictionary.com/) for the word lists