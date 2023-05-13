# Hangman Game

Hangman is a classic word guessing game. The player needs to guess the letters of a word within a limited number of tries. For each incorrect guess, a part of the hangman's body is drawn. If the player guesses all the letters before the hangman is complete, they win. Otherwise, they lose.

## Rules of the Game

1. A random word is chosen from a predefined word list.
2. The player can guess a letter or request a hint.
3. If the player guesses a letter that is in the word, it is revealed. Otherwise, the number of remaining tries decreases.
4. The player continues guessing until they either guess all the letters correctly and win or run out of tries and lose.
5. The player can request up to three hints throughout the game, each hint providing a definition of the word.

## How to Run the Game

To run the Hangman game, follow these steps:

1. Install the required dependencies by running the following command:
pip install requests python-dotenv

2. Create a file named `.env` in the same directory as the Python script (`hangman.py`).

3. In the `.env` file, add the following line, replacing `YOUR_API_KEY` with your WordsAPI API key:
API_KEY="YOUR_API_KEY"

4. Save the `.env` file.

5. Run the Python script `hangman.py` using the following command:
python hangman.py


## Dependencies

- `requests`: Used to make HTTP requests to the WordsAPI to fetch word definitions.
- `python-dotenv`: Used to load environment variables from the `.env` file.

## Acknowledgements

The Hangman game implementation uses the WordsAPI (https://www.wordsapi.com/) to provide word definitions as hints.

## Notes

- The word list in the game code is a sample list of words that can be customized or extended as per your preference.
- Make sure to replace `YOUR_API_KEY` in the `.env` file with your actual WordsAPI API key for the hint functionality to work properly.

Enjoy playing the Hangman game!
