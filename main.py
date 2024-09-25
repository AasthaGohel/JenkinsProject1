import random
import hangman_art
import hangman_words

# Function to load guesses from a text file
def load_guesses_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().splitlines()  # Read each line as a guess
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return []

def play_hangman(guesses):
    lives = 6
    print(hangman_art.logo)

    # Choose a word randomly from word_list
    chosen_word = random.choice(hangman_words.word_list)

    # Create a display list with underscores representing each letter in the chosen word
    display = ['_' for _ in range(len(chosen_word))]
    print(f"Word to guess: {display}")

    game_over = False
    guessed_letters = []
    guess_index = 0  # To track guesses from the input file

    while not game_over and guess_index < len(guesses):
        guess_letter = guesses[guess_index].lower()  # Read a guess from the file
        guess_index += 1

        # Check if the letter was already guessed
        if guess_letter in guessed_letters:
            print(f"You've already guessed '{guess_letter}'. Try a different letter.")
            continue

        guessed_letters.append(guess_letter)

        # Check if the guessed letter is in the chosen word
        if guess_letter in chosen_word:
            for position in range(len(chosen_word)):
                if chosen_word[position] == guess_letter:
                    display[position] = guess_letter
        else:
            lives -= 1
            print(f"'{guess_letter}' is not in the word. You lose a life.")
            if lives == 0:
                game_over = True
                print('You lose.')
                print(f"The word was: {chosen_word}")

        print(f"Current word: {display}")

        if '_' not in display:
            game_over = True
            print('You win!')

        # Display the hangman art
        print(hangman_art.stages[lives])

    # If game ended due to running out of guesses
    if guess_index >= len(guesses):
        print("No more guesses left.")
        if not game_over:
            print(f"The word was: {chosen_word}")

if __name__ == "__main__":
    # Load guesses from the 'guessed_words.txt' file
    guesses = load_guesses_from_file('guessed_words.txt')
    if guesses:
        play_hangman(guesses)
    else:
        print("No guesses to process.")
