# Basic Dice rolling code, feel free to use for your own needs.
# Rolls a x sided dice x times for x turns.
# Developer: ConfusedTomatoDev
# Created 08/16/2021 CTD
#
from random import randint

# Pick the number of dice sides
dice_sides = 20

# Pick the number of rolls per turn
dice_rolls = 20

# Pick the number of turns
turns = 5

# Counters
count_turns = 1

# Functions
def roll_dice():
    roll_count = 0
    while roll_count < dice_rolls:
        print(randint(1,dice_sides))
        roll_count += 1

# Main routine
while count_turns != turns+1:
    print ("\nRoll", count_turns,"\n")
    roll_dice()
    count_turns += 1
   
