import random


print("\nWelcome to Hangman game by IT SOURCECODE\n")


# The parameters we require to execute the game:
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["Mohamed", "Esmael", "january", "border", "image", "film", "promise", "kids", "lungs", "doll",
                      "rhyme", "damage", "plants", "faith", "chain", "rhyme", "fear", "shirt", "driving", "silver", ]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""

# A loop to re-execute the game when the first round ends:


def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game in ["y", "Y"]:
        main()
    elif play_game in ["n", "N"]:
        print("Thanks For Playing! We expect you back again!")
        exit()

# Initializing all the conditions required for the game:


def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 8
    guess = input("This is the Hangman Word: " +
                  display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

# Check if letter is entered more than one and is wrong:

    elif guess in already_guessed:
        print("Try another letter.\n")

    else:
        count += 1

        if count == 1:
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            print("   _____ \n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |       \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |       \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 5:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     |  \n"
                  "  |     o \n"
                  "  |       \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 6:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     |  \n"
                  "  |     o \n"
                  "  |     |\ \n"
                  "  |        \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 7:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     |  \n"
                  "  |     o  \n"
                  "  |    /|\ \n"
                  "  |        \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) +
                  " Last guesses remaining\n")

        elif count == 8:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("You guessed:", already_guessed)
            print("The word was:", word)
            play_loop()

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly! \n")
        print("       Thank You\n"
              " You Saved MY LIFE !\n"
              "       O \n"
              "      /|\ \n"
              "      / \ \n"
              "\n")
        play_loop()

    elif count != limit:
        hangman()


# Driver Code:
main()

hangman()
