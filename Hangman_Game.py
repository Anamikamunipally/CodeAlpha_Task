import random

def hangman():
    words = ["python", "program", "hangman", "internship", "codealpha"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6
    used_letters = []

    print("Welcome to Hangman Game!")
    print("Word:", " ".join(guessed))

    while attempts > 0 and "_" in guessed:
        guess = input("\nGuess a letter: ").lower()

        if guess in used_letters:
            print("You already guessed that letter!")
            continue

        used_letters.append(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
            print("Correct! Word:", " ".join(guessed))
        else:
            attempts -= 1
            print(f"Wrong! Attempts left: {attempts}")

    if "_" not in guessed:
        print("\n🎉 You Win! The word was:", word)
    else:
        print("\n😢 Game Over! The word was:", word)

if __name__ == "__main__":
    hangman()
