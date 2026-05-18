"""
MSIT Project - Snowman Meltdown
"""
import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    """Zeigt den aktuellen Zustand des Spiels an."""

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
    """Haiptspiel-Logik für Snowman Meltdown."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters) # Stage 0
        guess = input("Guess a letter: ").lower().strip()

        # Einfache Validierung der Benutzereingabe
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        # wir chcken, ob der Buchstabe schon geraten wurde
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        # Buchstabe zur Liste der geratenen Buchstaben hinzufügen
        guessed_letters.append(guess)

        # Überprüfen, ob der Buchstabe im geheimen Wort ist
        if guess not in secret_word:
            # Falscher Buchstabe, Fehler erhöhen
            mistakes += 1
            print("Wrong!")
        else:
            print("Correct!")

        # Gewinn ckecken
        won = True
        # Wir überprüfen, ob alle Buchstaben des geheimen Wortes geraten wurden
        for letter in secret_word:
            if letter not in guessed_letters:
                won = False
                break

        # Wenn gewonnen, Spiel beenden
        if won:
            display_game_state(mistakes, secret_word, guessed_letters)
            print("You won! You saved the snowman! The word was:", secret_word)
            return

    # sonst Verloren- auch Spiel beenden und das geheime Wort anzeigen
    display_game_state(mistakes, secret_word, guessed_letters)
    print("You lost! The snowman melted! The word was:", secret_word)

    # Benutzer fragen, ob er nochmal spielen will
    replay = input("Do you want to play again? (y/n): ").lower().strip()
    if replay == 'y':
        play_game()
    else:
        print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    play_game()
