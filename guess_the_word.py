"“”
Guess the Word Game
“”"

def get_display_word(word, guessed_letters):
    “”"Show word with guessed letters revealed”“”
    return ' ’.join([letter if letter in guessed_letters else ‘_’
                     for letter in word])

def play_game():
    print(“Welcome to Guess the Word!“)
    word = “python”
    guessed_letters = []
    max_attempts = 6
    incorrect_guesses = 0

    while incorrect_guesses < max_attempts:
        # Show current progress
        print(f”\nWord: {get_display_word(word, guessed_letters)}“)
        print(f”Guessed: {‘, ’.join(guessed_letters)}“)

        guess = input(“Guess a letter: “).lower()

        if guess in guessed_letters:
            print(“Already guessed!“)
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(“Correct!“)
            # Check if word is complete
            if all(letter in guessed_letters for letter in word):
                print(f”You won! The word was: {word}“)
                break
        else:
            incorrect_guesses += 1
            print(f”Wrong! {max_attempts - incorrect_guesses} attempts left”)
    else:
        print(f”Game Over! The word was: {word}“)

if __name__ == “__main__“:
    play_game()
