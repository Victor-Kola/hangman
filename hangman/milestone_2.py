import random
word_list = ["banana", "watermelon", "apple", "cherries", "black grapes"]
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Please input a letter " ) 

if guess == 1 and guess.isalpha() == True:
    print("Good guess!")
else:
    print("Oops! That is not a valid input")
    
