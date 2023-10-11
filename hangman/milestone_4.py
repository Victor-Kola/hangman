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

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.num_lives = num_lives
        self.word = word
        self.word_guessed = list(word).join(['_' for char in list])
        self.num_letters = len(word)
        self.word_list = favourite_fruits
        self.list_of_guesses = []

