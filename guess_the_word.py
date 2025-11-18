"“”
Guess the Word Game
“”"
import random

class WordGuessingGame:
    “”"A class to represent the word-guessing game.“”"

    def __init__(self, word_list=None, max_attempts=6):
        if word_list is None:
            self.word_list = [
                “python”, “programming”, “computer”, “algorithm”,
                “function”, “variable”, “database”, “network”,
                “software”, “hardware”, “developer”, “testing”
            ]
        else:
            self.word_list = word_list

        self.max_attempts = max_attempts
        self.word = self.select_word()
        self.guessed_letters = set()
        self.incorrect_guesses = 0
        self.game_over = False
        self.won = False

    def select_word(self):
        “”"Select a random word from the word list.“”"
        return random.choice(self.word_list).lower()

    def get_display_word(self):
        “”"Get current state of word with guessed letters revealed.“”"
        return ' ’.join([letter if letter in self.guessed_letters else ‘_’
                        for letter in self.word])

    def guess_letter(self, letter):
        “”"Process a letter guess with detailed feedback.“”"
        # Validate input
        if not letter or len(letter) != 1:
            return {
                ‘valid’: False,
                ‘correct’: False,
                ‘already_guessed’: False,
                ‘message’: ‘Please enter a single letter.’
            }

        letter = letter.lower()

        if not letter.isalpha():
            return {
                ‘valid’: False,
                ‘correct’: False,
                ‘already_guessed’: False,
                ‘message’: ‘Please enter a valid letter (a-z).’
            }

        if letter in self.guessed_letters:
            return {
                ‘valid’: True,
                ‘correct’: False,
                ‘already_guessed’: True,
                ‘message’: f’You already guessed “{letter}“.'
            }

        self.guessed_letters.add(letter)

        if letter in self.word:
            # Check if word is complete
            if all(letter in self.guessed_letters for letter in self.word):
                self.game_over = True
                self.won = True

            return {
                ‘valid’: True,
                ‘correct’: True,
                ‘already_guessed’: False,
                ‘message’: f’Good guess! “{letter}” is in the word.'
            }
        else:
            self.incorrect_guesses += 1

            if self.incorrect_guesses >= self.max_attempts:
                self.game_over = True
                self.won = False

            return {
                ‘valid’: True,
                ‘correct’: False,
                ‘already_guessed’: False,
                ‘message’: f’Sorry, “{letter}” is not in the word.'
            }

    def get_remaining_attempts(self):
        “”"Get number of remaining incorrect guesses allowed.“”"
        return self.max_attempts - self.incorrect_guesses

    def is_word_guessed(self):
        “”"Check if entire word has been guessed.“”"
        return all(letter in self.guessed_letters for letter in self.word)

def play_game():
    print(“=” * 50)
    print(“Welcome to Guess the Word!“)
    print(“=” * 50)
    print(“\nTry to guess the word one letter at a time.“)
    print(“You have 6 incorrect guesses before you lose.\n”)

    game = WordGuessingGame()

    while not game.game_over:
        print(f”\nWord: {game.get_display_word()}“)
        print(f”Guessed letters: {‘, ’.join(sorted(game.guessed_letters)) if game.guessed_letters else ‘None’}“)
        print(f”Remaining attempts: {game.get_remaining_attempts()}“)

        guess = input(“\nGuess a letter: “).strip()
        result = game.guess_letter(guess)
        print(result[‘message’])

        if game.game_over:
            print(“\n” + “=” * 50)
            if game.won:
                print(“:tada: CONGRATULATIONS! :tada:”)
                print(f”You guessed the word: {game.word.upper()}“)
            else:
                print(“:disappointed: GAME OVER! :disappointed:”)
                print(f”The word was: {game.word.upper()}“)
            print(“=” * 50)

if __name__ == “__main__“:
    play_game()
