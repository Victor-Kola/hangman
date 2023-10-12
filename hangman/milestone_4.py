import random
print(favourite_fruits)


class Hangman:
    """This is a class to represent the game of Hangman.
    
    
    Attributes:
    ---------
    
    word : str 
        The word to be guessed in the game
    
    word_guessed : list
        A list representation of the word to be guessed with the guessed letters revealed as the game goes on and _ for any unknown letters.
    
    unique_letters : set 
        A set containing all the unique letters in the word to be guessed. 
        
    num_lives : int
        An int value of the number of lives the players has that starts at 5 """
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list).lower()
        self.word_guessed = ["_"]*len(word)
        self.unique_letters = set(self.word)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guessed_letter):
        lowercase_guess = guessed_letter.lower()

        if lowercase_guess in self.unique_letters:
            print(f"Good GUESS! {lowercase_guess} is in the word.")
            for index, char in enumerate(self.word):
                if lowercase_guess in self.word:
                    position = self.word.index(lowercase_guess)
                    self.word_guessed[position] = lowercase_guess
            self.unique_letters.remove(lowercase_guess) 
        else:
            print(f"Sorry, {lowercase_guess} is not in the word. Try again")
            self.num_lives -= 1 
            print(f"You have {self.num_lives} left.")

    def ask_for_input(self):
        while True:
            guessed_letter = input("Guess a letter ")
            if len(guessed_letter) != 1 or not guessed_letter.isalpha():
                print("Invalid letter. Please enter a single alphabetical character.")
            elif guessed_letter in self.list_of_guesses:
                print("You already tried that letter.")
            else:
                self.check_guess(guessed_letter)
                self.list_of_guesses.append(guessed_letter)
                break

favourite_fruits = ["banana", "watermelon", "apple", "cherries", "black grapes"]
game = Hangman(favourite_fruits)
result = game.ask_for_input()
