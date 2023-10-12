# Victor's Hangman Game 

## Overview

This is my take on the classic Hangman game that picks a word at random from a list of words and asks the user to pick a word at random each time. After each guess, the game provides feedback so the player knows whether or not they are on the right track or not. The game ends when the player guesses all letters correctly or runs out of lives.

## Features

Random word selection: The game selects a word to guess from a list of words. 
Guessing feedback: After each succesful guess the game provides feedback.
Limited lives: The game will terminate when the guesses are incorrect after a certain number of times. The players have limited lives. 
Dynamic display: After each guess, the game displays the current state of the game and where he player is.

## How to use 

1. Run the Python script.
2. The game will ask you to guess a letter in the terminal.
3. Enter a letter in the terminal.
4. The game will display whether you were right, if so it will display the status of the game, if wrong it will tel l you to try again.
5. Continue guessing until you run out of lives or you win.


## File structure 
1. Hangman Class:  This represents main bulk of the game and contains the methods necessary to run the game. Including checking the guess and asking for an input. 
2. play_game function: This function runs the game. It runs the Hangman class, manages the game and ends the game when required.

## What I learned

I learned quite a bit while developing this game. It was the first opportunity to bring together the basics of python with OOP while also creating a project that is set up in github. I learnt how to update my projects on github. I also learnt how to create a game, create commands to run a game and manage a game programme. I thnik the biggest key takeaway for me was writing out code and then optimising code at each step so as to not repeat code but also make it more readable. 
The second biggest takeaway was like I said, bringing all my knowledge together and being able to find the answers for what I need on stack overflow / google .

## Limitations

If word list is changed and contains a word with a space, this word cannot be accessed as the user can't input a space. The code doesn't account for words with spaces.


# Milestone_3 brief overview 


We have updated milestone 3 to create two functions that wil ask our user for their input and check if their input is in the random word we have generated. What we have learned so far is how to convert words to lowercase, define functions and also utilising while and for loops. 

# Milestone_4 brief overview 

We have updated milestone 4 to define the hangman class, we have created two methods for this class which include, checking the guess and askking for input. The aim of this part of the project is to create an instance of the Hangman game that should be played, reduce the players life when they get it wrong but then also replace the missing letter if they get it right. 

