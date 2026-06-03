"""Main funktion zum Starten des Spiels."""
from game_logic import play_game

def main():
    """Startet das Snowman Meltdown Spiel."""
    print("Welcome to Snowman Meltdown!")
    while True:
        play_game()
        # Replay abfragen mit validierung in eine innere Schleife
        while True:
            replay = input("Would you like to play again? (y/n): ")
            if replay == "y":
                break
            if replay == "n":
                print("Thank you. Goodbye!")
                # beende die main
                return
            else:
                print("please enter y or n")

if __name__ == "__main__":
    main()
