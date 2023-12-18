# SimplyFI_Assignment

# Question 1: convert_to_indian_currency
# 1)convert_to_indian_currency function:

It takes an integer num as input.
Converts the integer num into a string representation num_str.
Determines the length of the string (num_len).
If the length of the number is less than or equal to 3 (i.e., the number has 3 digits or less), it simply returns the string representation of the number.

# 2)For numbers with more than 3 digits:
It initializes an empty list groups to store separated groups of digits.
Enters a loop while the length of the number string is greater than 0.
Splits the number string into groups of three digits from the end (right side) and appends these groups to the groups list.
Reduces the length of the number string and moves to the next group of three digits until the entire number is separated.
Reverses the order of groups to arrange them correctly.
Joins the groups together with commas between them using ",".join(groups) and returns the final formatted string.

# 3)Example usage:
It demonstrates the usage of the convert_to_indian_currency function.
Initializes an amount variable with a value of 504678.
Calls the convert_to_indian_currency function with amount and stores the result in indian_currency_format.
Prints the original input amount (amount) and the formatted output (indian_currency_format).
Output:

# The code prints the input amount (504678) and the output in Indian currency notation (5,04,678), which separates the digits of the given number with commas to represent it in Indian currency format.


# Question 2 Explanation:

# 1)Function min_players_to_be_shot:

This function takes three arguments: N (number of players), K (height of Gi-Hun and Ali), and heights (a list of heights of players between Gi-Hun and Ali).
It iterates through the heights of the players between Gi-Hun and Ali.
For each player's height, it checks if the height is greater than K (the height of Gi-Hun and Ali). If so, it increments the count variable.
Finally, it returns the total count of players taller than Gi-Hun and Ali.

# 2)Reading Input and Processing:

T = int(input()): Reads the number of test cases.
for _ in range(T):: Iterates through each test case.
N, K = map(int, input().split()): Reads N (number of players) and K (height of Gi-Hun and Ali) for the current test case.
heights = list(map(int, input().split())): Reads the heights of the players between Gi-Hun and Ali and stores them in a list.
Calls the min_players_to_be_shot function with the test case details to calculate the minimum number of players needed to be removed for Ali to be visible to Gi-Hun.
Prints the result for each test case.

# 3)Execution:

The code reads the number of test cases.
For each test case, it processes the input by extracting the number of players, the height of Gi-Hun and Ali, and the heights of the players between them.
It then calculates and prints the minimum number of players that need to be shot for Ali to be visible to Gi-Hun for each test case.

