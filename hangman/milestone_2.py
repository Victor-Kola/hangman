import random
favourite_fruits = ["banana", "watermelon", "apple", "cherries", "black grapes"]
print(favourite_fruits)

word = random.choice(favourite_fruits)
print(word)

guessed_letter = input("Please input a letter " ) 

if len(guessed_letter) == 1 and guessed_letter.isalpha() == True:
    print("Good guess!")
else:
    print("Oops! That is not a valid input")
    
