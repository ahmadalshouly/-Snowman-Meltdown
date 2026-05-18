import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
   # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")

def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters) # Stage 0
        guess = input("Guess a letter: ").lower().strip()

        guessed_letters.append(guess)

        if guess not in secret_word:
            mistakes += 1
            print("Wrong!")
        else:
            print("Correct!")

        # Gewinn ckecken
        won = True
        for letter in secret_word:
            if letter not in guessed_letters:
                won = False
                break

        if won:
            display_game_state(mistakes, secret_word, guessed_letters)
            print("You won! You saved the snowman! The word was:", secret_word)
            return

    # sonst Verloren
    display_game_state(mistakes, secret_word, guessed_letters)
    print("You lost! The snowman melted! The word was:", secret_word)

if __name__ == "__main__": 
    play_game()