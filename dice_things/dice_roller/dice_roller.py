# Basic Dice rolling code, feel free to use for your own needs.
# Rolls a x sided dice x times for x turns.
# Developer: ConfusedTomatoDev
# Created 08/16/2021
#
from random import randint

# Pick the number of dice sides
dice_sides = 20

# Pick the number of rolls per turn
dice_rolls = 20

# Pick the number of turns
turns = 5

# Counters and lists
count_turns = 1
average_list = []

# Functions
def roll_dice():
    roll_count = 0
    print ("Rolling...")
    while roll_count < dice_rolls:
        roll = (randint(1,dice_sides))
        # Uncomment line below if you need vertical list of rolls
        #print (roll)
        roll_count += 1
        average_list.append(roll)
        
# Main routine
while count_turns != turns+1:
    print("Turn:", count_turns)
    roll_dice()
    print("Rolls: " + ", ".join(map(str, average_list)))
    #print ("Averaging")
    average_total = sum(average_list) / len(average_list)
    #print ("Done averaging")
    print("Average:", round(average_total))
    print("============================\n")
    average_list.clear()
    count_turns += 1
