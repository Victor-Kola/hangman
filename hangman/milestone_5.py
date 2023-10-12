import random

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
        An int value of the number of lives the players has that starts at 5 and decreases as the game goes on.
    
    word_list : list
        A list containing the bank of potential words that can be drawn within the game.
        
    list_of_guesses: list
        A list containing all the potential alphabetical letters that have been input by the player. """
    def __init__(self, word_list, num_lives = 5):
        """ Initializes the Hangman game with a given word and number of lives.

        Parameters:
        ----------

        word_list : list
            A list containing the bank of potential words that can be drawn within the game.

        num_lives : int
            An int value of the number of lives the players has that starts at 5 and decreases as the game goes on.
        
        """
        self.word = random.choice(word_list).lower()
        self.word_guessed = ["_"]*len(self.word)
        self.unique_letters = set(self.word)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []


    def check_guess(self, guessed_letter):
        """ 
        Checks the guess that was input by the player. 

        Parameters:
        ----------
        guessed_letter : str 
            The letter guessed by the player.
        
        
        """
        lowercase_guess = guessed_letter.lower()

        if lowercase_guess in self.unique_letters:
            print(f"Good GUESS! {lowercase_guess} is in the word.")
            for index, char in enumerate(self.word):
                if char in lowercase_guess:
                    position = self.word.index(lowercase_guess)
                    self.word_guessed[index] = lowercase_guess
            self.unique_letters.remove(lowercase_guess) 
        else:
            print(f"Sorry, {lowercase_guess} is not in the word. Try again")
            self.num_lives -= 1 
            print(f"You have {self.num_lives} left.")

    def ask_for_input(self):
        """
        Asks the player for their input into the game.
        """
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


def play_game(word_list):
    """
    Runs the game """  
    num_lives = 5
    game = Hangman(word_list, num_lives)    
    print(game.word_guessed)
    while True:
        if num_lives == 0:
            print("You lost!")
        if len(game.unique_letters) > 0:
           game.ask_for_input()
           print(game.word_guessed)
        if game.num_lives != 0 and len(game.unique_letters) <= 0:
            print("Congratulations. You've won the game!")
            break

favourite_fruit = ["banana", "watermelon", "apple", "cherries", "black grapes"]

play_game(favourite_fruit)


