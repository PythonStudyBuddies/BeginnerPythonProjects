# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 11:32:49 2020

@author: Dylan
"""


import random
number = random.randint(1, 100)
player_name = input("Hello, what's your name?")

number_of_guesses = 0

print('Okay! '  + player_name + ' I am guessing a number between 1 and 100: ')

while number_of_guesses < 10:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print("Guess is too low!")
    if guess > number:
        print("Guess is too high!")
    if guess == number: 
        break
if guess == number :
    print('Good guess! It took you ' + str(number_of_guesses) + ' tries to get it!')
else:
    print('Unlucky, the number was ' + str(number))