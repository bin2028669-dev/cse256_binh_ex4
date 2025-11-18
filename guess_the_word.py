"“”
Guess the Word Game
“”"
import random

def get_display_word(word, guessed_letters):
    return ' ’.join([letter if letter in guessed_letters else ‘_’
                     for letter in word])

def validate_guess(guess, guessed_letters):
    “”"Validate user input”“”
    if not guess or len(guess) != 1:
        return False, “Please enter a single letter.”

    if not guess.isalpha():
        return False, “Please enter a valid letter (a-z).”

    if guess in guessed_letters:
        return False, f”You already guessed ‘{guess}‘.”

    return True, “”

def play_game():
    print(“=” * 50)
    print(“Welcome to Guess the Word!“)
    print(“=” * 50)

    word_list = [“python”, “programming”, “computer”, “algorithm”,
                 “function”, “variable”, “database”, “network”]
    word = random.choice(word_list).lower()

    guessed_letters = []
    max_attempts = 6
    incorrect_guesses = 0

    while incorrect_guesses < max_attempts:
        print(f”\nWord: {get_display_word(word, guessed_letters)}“)
        print(f”Guessed: {‘, ’.join(sorted(guessed_letters)) if guessed_letters else ‘None’}“)
        print(f”Remaining attempts: {max_attempts - incorrect_guesses}“)

        guess = input(“\nGuess a letter: “).strip().lower()

        # Validate input
        valid, message = validate_guess(guess, guessed_letters)
        if not valid:
            print(message)
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f”Good guess! ‘{guess}’ is in the word.“)
            if all(letter in guessed_letters for letter in word):
                print(f”\nCONGRATULATIONS! You guessed: {word.upper()}“)
                break
        else:
            incorrect_guesses += 1
            print(f”Sorry, ‘{guess}’ is not in the word.“)
    else:
        print(f”\nGAME OVER! The word was: {word.upper()}“)

if __name__ == “__main__":
    play_game()
