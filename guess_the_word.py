"“”
Guess the Word Game
“”"

def play_game():
    print(“Welcome to Guess the Word!“)
    word = “python”
    guessed_letters = []
    max_attempts = 6
    incorrect_guesses = 0

    while incorrect_guesses < max_attempts:
        guess = input(“Guess a letter: “).lower()

        if guess in guessed_letters:
            print(“Already guessed!“)
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(“Correct!“)
        else:
            incorrect_guesses += 1
            print(f”Wrong! {max_attempts - incorrect_guesses} attempts left”)

    print(f”Game Over! The word was: {word}“)

if __name__ == “__main__“:
    play_game()
