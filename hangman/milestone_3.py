import random
favourite_fruits = ["banana", "watermelon", "apple", "cherries", "black grapes"]
print(favourite_fruits)

word = random.choice(favourite_fruits)




def check_guess(guessed_letter):
    lowercase_guess = guessed_letter.lower()
    if guessed_letter in word:
        print(f"Good GUESS! {guessed_letter} is in the word.")
    else:
        print(f"Sorry, {guessed_letter} is not in the word. Try again")

def ask_for_input():
    while True:
        guessed_letter = input("Guess a letter ")
        if len(guessed_letter) == 1 and guessed_letter.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character")
    check_guess(guessed_letter)

ask_for_input()

