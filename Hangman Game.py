import random

def hangman():
    # Step 1: Predefined word list
    words = ["python", "hangman", "coding", "program", "simple"]
    word = random.choice(words)  # Randomly select word

    guessed = []  # Already guessed letters
    attempts = 6  # Incorrect guess limit

    print("Welcome to Hangman Game!")
    print("You have 6 chances to guess the word.\n")

    # Step 2: Game loop
    while attempts > 0:
        # Show current word with guessed letters
        display_word = ""
        for letter in word:
            if letter in guessed:
                display_word += letter + " "
            else:
                display_word += "_ "
        print("Word:", display_word.strip())

        # Check if word guessed completely
        if all(letter in guessed for letter in word):
            print("\n Congratulations! You guessed the word:", word)
            break

        # Step 3: Take input from player
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only a single alphabet.\n")
            continue

        if guess in guessed:
            print(" You already guessed this letter.\n")
            continue

        guessed.append(guess)

        # Step 4: Check guess
        if guess in word:
            print(" Correct guess!\n")
        else:
            attempts -= 1
            print("Wrong guess! Attempts left:", attempts, "\n")

    else:
        print("\n Sorry, you ran out of attempts. The word was:", word)


# Run the game
hangman()
