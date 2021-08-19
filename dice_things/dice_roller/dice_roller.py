# Basic Dice rolling code, feel free to use for your own needs.
# Rolls a x sided dice x times for x turns.
# and returns the following: average, min, lower quaderant, median, upper quaderant, max, mean, stdv, frequency table.
# Written in a rush, code is not pretty, rules were not followed, needed it for homework assignment, it's a PoC that worked for what it had to do....
#
# Developer: ConfusedTomatoDev
# Created 08/16/2021
#
# Sites that helped with how to formulate and present the numbers.
# https://www.mathsisfun.com/data/quartiles.html
# https://www.hackmath.net/en/calculator/quartile-q1-q3
#
import statistics
import numpy as npmath
from random import randint
from statistics import mean

# Input dice info
while True:
  try:
    dice_sides = int(input("Enter number of sides on the dice: "))
    if dice_sides>1 and dice_sides<=120:
      print("Dice sides entered successfully...")
      break;
    else:
      print("Disce sides should be greater than 1 and equal to or less than 120...")
  except ValueError:
    print("Provide an numeric value only...")
    continue

while True:
  try:
    dice_rolls = int(input("Enter number of times to roll the dice between turns: "))
    if dice_rolls>0 and dice_rolls<=1000:
      print("Dice rolls entered successfully...")
      break;
    else:
      print("Disce sides should be greater than 0 and equal to or less than 1000...")
  except ValueError:
    print("Provide an numeric value only...")
    continue

while True:
  try:
    turns = int(input("Enter number of turns to roll the dice: "))
    if turns>0 and turns<=1000:
      print("Dice turns entered successfully...")
      break;
    else:
      print("Disce turns should be greater than 0 and equal to or less than 1000...")
  except ValueError:
    print("Provide an numeric value only...")
    continue

# Counters and lists
count_turns = 1
roll_list = []
average_list = []


# Classes/Objects
# None yet

# Functions
def roll_dice():
	roll_count = 0
	print("Rolling...")
	while roll_count < dice_rolls:
		roll = (randint(1, dice_sides))
		# Uncomment line below if you need vertical list of rolls
		#print (roll)
		roll_count += 1
		roll_list.append(roll)


def CountFrequency(average_list):
	# Creating an empty dictionary
	freq = {}
	for item in average_list:
		if (item in freq):
			freq[item] += 1
		else:
			freq[item] = 1
	for key, value in freq.items():
		#print (key ,"     ", value)
		print(f'{key:3d}    {value:3d}')


# Main routine
while count_turns != turns + 1:
	print("Turn number:", count_turns)
	roll_dice()
	print("Roll: " + ", ".join(map(str, roll_list)))
	roll_list.sort()
	print("Sorted Roll: " + ", ".join(map(str, roll_list)))
	#print("Done Rolling, calculating...")
	#print ("Averaging...")
	average_ans = sum(roll_list) / len(roll_list)
	average_list.append(round(average_ans))
	#print ("Done averaging...")
	print("Average of roll:", round(average_ans))
	print("\n")
	print("Average each turn: " + ", ".join(map(str, average_list)))
	average_list.sort()
	print("Sorted average of each turn: " + ", ".join(map(str, average_list)))
	print("\n")
	print("Minimum value of average turns:", min(average_list))
	print("Rounded minimum value of average turns:", round(min(average_list)))
	print("\n")
	print("Q1 quantile of average turns: ", npmath.quantile(average_list, .25))
	print("Rounded Q1 quantile of average turns: ", round(npmath.quantile(average_list, .25)))
	print("Q2 quantile of average turns: ", npmath.quantile(average_list, .50))
	print("Rounded Q2 quantile of average turns: ", round(npmath.quantile(average_list, .50)))
	print("Q3 quantile of average turns: ", npmath.quantile(average_list, .75))
	print("Rounded Q3 quantile of average turns: ", round(npmath.quantile(average_list, .75)))
	print("\n")
	print("Maximum value of average turns:", max(average_list))
	print("Rounded maximum value of average turns:", round(max(average_list)))
	print("\n")
	print("Mean of turns:", mean(average_list))
	print("Rounded mean of turns:", round(mean(average_list)))
	print("Median of turns:", npmath.median(npmath.array(average_list)))
	print("Rounded median of turns:", round(npmath.median(npmath.array(average_list))))
	res = statistics.pstdev(average_list)
	print("Standard deviation of turns: " + str(res))
	print("Rounded standard deviation turns: ", round(res))
	print("\n")
	print("Data frequency of average from turns:")
	print("-------------------------------------")
	print("Data    Freq")
	CountFrequency(average_list)
	print("=====================================\n")
	print("Results are based on the following: Number of dice sides:", dice_sides, " Number of dice rolls:", dice_rolls, " Number of turns:", turns, "\n")
	roll_list.clear()
	count_turns += 1
