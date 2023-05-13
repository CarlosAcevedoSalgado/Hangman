import requests
import random
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# constants
API_KEY = os.getenv("API_KEY")
HINT_API_URL = "https://wordsapiv1.p.rapidapi.com/words/{}/definitions"

# return a random word from the internet
def get_random_word():
    word_list = ['apple', 'banana', 'orange', 'pear', 'grape', 'kiwi', 'melon', 'lemon', 'peach', 'cherry', 'strawberry', 'pineapple', 'coconut', 'watermelon', 'avocado', 'blueberry', 'raspberry', 'blackberry', 'plum', 'papaya']
    return random.choice(word_list)

# Get word definition using WordsAPI
def get_word_definition(word):
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
    }

    try:
        response = requests.get(HINT_API_URL.format(word), headers=headers)
        response.raise_for_status()
        data = response.json()
        if "definitions" in data:
            definitions = []
            for definition in data["definitions"]:
                definitions.append(definition["definition"])
            return definitions
    except requests.exceptions.RequestException as e:
        print("Error occurred while fetching the word definitions:", str(e))
    return None

# the main function of the game
def hangman(): 
    word = get_random_word() # get a random word
    # Check if the word is None (no word found) and exit the game
    if word is None:
        print("Failed to get a random word. Exiting the game.")
        return
    
    guessed_letters = [] # list of letters guessed by the user
    tries = 6 # 6 tries to guess the word
    hints_given = 0 # number of hints given to the user

    # loop until the user has no more tries or the word is guessed
    while tries > 0:
        # Display the current status of the word with blanks for unguessed letters
        display_word = display_word = ''.join(letter if letter in guessed_letters else '_ ' for letter in word)
        print("Current word:", display_word) # display the current word with the guessed letters and blanks for unguessed letters

        # Ask the player to guess a letter
        guess = input("Guess a letter or type 'hint' to get a hint: ").lower()

        if guess == "hint":
            if hints_given == 3:
                print("You've already used all 3 hints for this word.")
                continue
            else:
                definitions = get_word_definition(word)
                if definitions:
                    if hints_given < len(definitions):
                        print("Hint:", definitions[hints_given])
                        hints_given += 1
                    else:
                        print("No more hints available for this word.")
                else:
                    print("Failed to retrieve hints. Please try again.")
                continue

        # Check if the guessed letter is valid
        if len(guess) != 1 or not guess.isalpha():
            print("\nInvalid input. Please enter a single letter.")
            continue

        # Check if the guessed letter is already guessed
        if guess in guessed_letters:
            print("\nYou've already guessed that letter. Try again.")
            continue

        # Add the guessed letter to the list of guessed letters
        guessed_letters.append(guess)

        # Check if the guessed letter is in the word
        if guess in word:
            print("\nCorrect guess!")
            # Check if the player has won
            if all(letter in guessed_letters for letter in word):
                print("Congratulations! You've won!")
                break
        else:
            print("\nWrong guess!")
            tries -= 1
            print("You have", tries, "tries left.")
            # If the player runs out of tries
            if tries == 0:
                print("You lost. The word was:", word)

# Start the game
hangman()

