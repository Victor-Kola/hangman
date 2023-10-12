import random
favourite_fruits = ["banana", "watermelon", "apple", "cherries", "black grapes"]
print(favourite_fruits)

word = random.choice(favourite_fruits)
list_of_guesses = []
class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word = word
        self.word_guessed = ["_"]*len(word)
        self.num_letters = set(char for char in word.lower())
        self.num_lives = num_lives
        self.word_list = favourite_fruits
        self.list_of_guesses = list_of_guesses 

    def check_guess(self, guessed_letter):
        lowercase_guess = guessed_letter.lower()
        if lowercase_guess in self.word:
            print(f"Good GUESS! {lowercase_guess} is in the word.")
        else:
            print(f"Sorry, {lowercase_guess} is not in the word. Try again")

    def ask_for_input(self):
        while True:
            guessed_letter = input("Guess a letter ")
            if len(guessed_letter) > 1:
                print("Invalid letter. Please enter a single alphabetical character.")
            elif guessed_letter in list_of_guesses:
                print("You already tried that letter.")
            else:
                self.check_guess(guessed_letter)
                list_of_guesses.append(guessed_letter)
            if len(guessed_letter) == 1 and guessed_letter.isalpha():
                break


game = Hangman(favourite_fruits)
result = game.ask_for_input()
