"“”
Guess the Word Game
“”"

def play_game():
    “”"Main game function”“”
    print(“Welcome to Guess the Word!“)
    word = “python”
    print(f”The word has {len(word)} letters”)

    guess = input(“Guess a letter: “)
    if guess in word:
        print(“Correct!“)
    else:
        print(“Wrong!“)

if __name__ == “__main__“:
    play_game()
