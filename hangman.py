"A simple hangman game coded by Baguettifer and Copilot."

"(github.com/baguettifer/)"
"(copilot.github.com/)"

import random

random_words = ["python", "java", "kotlin", "javascript",]

quit = False

def play_handman():
    random_number = random.randint(0, len(random_words) - 1)

    wrong_guesses = 0

    word = random_words[random_number]

    #make a blank list which is the same length of random_words
    blank_list = ["_"] * len(word)

    while wrong_guesses != 6 and word != "".join(blank_list):

        #print the blank list
        print(" ".join(blank_list))

        #get input from user
        guess = input("Guess a letter: ")

        #check if the guess is "quit"
        if guess == "quit":
            return

        #check if letter is in word
        if guess in word:
            for i in range(len(word)):
                if guess == word[i]:
                    blank_list[i] = guess
        else:
            wrong_guesses += 1
            print("No, that letter is not in the word.", "You have", 6 - wrong_guesses, "guesses left.")

    if wrong_guesses == 6:
        print("You lose!", "The word was", word)
    else:
        print("You win!", "The word was", word.upper(), "Guesses left:", 6 - wrong_guesses)

def main():
    while True and not quit:
        play_handman()
        play_again = input("Play again? (Y/n): ").lower()
        if play_again == "n":
            break

if __name__ == "__main__":
    main()
