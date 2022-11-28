import random

words_to_guess = ["Mohamed", "Esmael", 'computer', 'science', 'programming',
                  'python', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board']
secret_word = random.choice(words_to_guess)
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter Guess : ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of Guesses, You Lost!")
else:
    print("You Win!")
