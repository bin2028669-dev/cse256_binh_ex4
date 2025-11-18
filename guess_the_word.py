"“”
Guess the Word Game
“”"

import random


class WordGuessingGame:
    “”"
    A class to represent the word-guessing game.

    Attributes:
        word_list (list): List of possible words to guess
        max_attempts (int): Maximum number of incorrect guesses allowed
        word (str): The word to be guessed
        guessed_letters (set): Set of letters that have been guessed
        incorrect_guesses (int): Count of incorrect guesses made
        game_over (bool): Flag indicating if the game has ended
        won (bool): Flag indicating if the player won
    “”"

    def __init__(self, word_list=None, max_attempts=6):
        “”"
        Initialize the game with a word list and maximum attempts.
        “”"
        if word_list is None:
            self.word_list = [
                “python”, “programming”, “computer”, “algorithm”, “function”,
                “variable”, “database”, “network”, “software”, “hardware”,
                “developer”, “testing”, “debugging”, “interface”, “terminal”
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
        “”"
        Select a random word from the word list.
        “”"
        return random.choice(self.word_list).lower()

    def get_display_word(self):
        “”"
        Get the current state of the word with guessed letters revealed.
        “”"
        return ' ’.join([letter if letter in self.guessed_letters else ‘_’
                        for letter in self.word])

    def guess_letter(self, letter):
        “”"
        Process a letter guess.
        “”"
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

        # Check if already guessed
        if letter in self.guessed_letters:
            return {
                ‘valid’: True,
                ‘correct’: False,
                ‘already_guessed’: True,
                ‘message’: f’You already guessed “{letter}“.'
            }

        # Add to guessed letters
        self.guessed_letters.add(letter)

        # Check if letter is in word
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

            # Check if out of attempts
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
        “”"
        Get the number of remaining incorrect guesses allowed.
        “”"
        return self.max_attempts - self.incorrect_guesses

    def is_word_guessed(self):
        “”"
        Check if the entire word has been guessed.
        “”"
        return all(letter in self.guessed_letters for letter in self.word)

    def get_game_state(self):
        “”"
        Get the current state of the game.
        “”"
        return {
            ‘word’: self.word,
            ‘display_word’: self.get_display_word(),
            ‘guessed_letters’: sorted(list(self.guessed_letters)),
            ‘incorrect_guesses’: self.incorrect_guesses,
            ‘remaining_attempts’: self.get_remaining_attempts(),
            ‘game_over’: self.game_over,
            ‘won’: self.won
        }


def play_game():
    “”"
    Main function to play the word-guessing game interactively.
    “”"
    print(“_” * 50)
    print(“Welcome to Guess the Word!“)
    print(“_” * 50)
    print(“\nTry to guess the word one letter at a time.“)
    print(“You have 6 incorrect guesses before you lose.\n”)

    # Initialize game
    game = WordGuessingGame()

    # Game loop
    while not game.game_over:
        # Display current state
        print(f”\nWord: {game.get_display_word()}“)
        print(f”Guessed letters: {‘, ’.join(sorted(game.guessed_letters)) if game.guessed_letters else ‘None’}“)
        print(f”Remaining attempts: {game.get_remaining_attempts()}“)

        # Get user input
        guess = input(“\nGuess a letter: “).strip()

        # Process guess
        result = game.guess_letter(guess)
        print(result[‘message’])

        # Check game status
        if game.game_over:
            print(“\n” + “_” * 50)
            if game.won:
                print(“CONGRATULATIONS!”)
                print(f”You guessed the word: {game.word.upper()}“)
                print(f”Total incorrect guesses: {game.incorrect_guesses}“)
            else:
                print(“GAME OVER!”)
                print(f”The word was: {game.word.upper()}“)
            print(“_” * 50)

    # Ask to play again
    play_again = input(“\nWould you like to play again? (yes/no): “).strip().lower()
    if play_again in [‘yes’, ‘y’]:
        print(“\n” * 2)
        play_game()  # Recursive call for replay
    else:
        print(“\nThanks for playing! Goodbye!“)


if __name__ == “__main__“:
    play_game()
