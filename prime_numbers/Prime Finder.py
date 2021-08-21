# Python3 program to display first N Prime numbers
# Written in a rush, code is not pretty, rules were not followed, needed it for homework assignment, it's a PoC that worked for what it had to do....
#
# Developer: ConfusedTomatoDev
# Created 08/20/2021
#

# Function prints prime numbers up to N
def print_primes_till_N(N):

	# Define the variables
	i, j, flag = 0, 0, 0;

	# Print display message
	print("Found these prime numbers between 1 and",N , "are:");

	# Loop for each number from 1 to N
	for i in range(1, N + 1, 1):

		# Skip 0 and 1 as they are not prime or composite numbers
		if (i == 1 or i == 0):
			continue;

		# Mark variable and check see if it is prime or not
		flag = 1;

		for j in range(2, ((i // 2) + 1), 1):
			if (i % j == 0):
				flag = 0;
				break;
		# flag = 1 means  it is prime and flag = 0 means it is not prime
		if (flag == 1):
			print(i, end = " ");

# Main routine
N = 1000;
print_primes_till_N(N);
