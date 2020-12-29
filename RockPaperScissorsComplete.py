# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 12:09:54 2020

@author: Dylan
"""
#To make this more challenging, find a way to decrease human error.

from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

# set player to False
player = False

while player == False:
    #set player to true
    player = input("Rock, Paper, Scissors?").capitalize().replace(" ", "")
    if player == computer:
        print("Tie! We both win!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer,"covers", player)
        else:
            print("You Win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer,"cuts", player)
        else:
            print("You Win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!", computer,"smashes", player)
        else:
            print("You Win!", player, "cut", computer)
    else:
        print("Wrong input value! Check your spelling!")
    player = False
    computer =t[randint(0,2)]