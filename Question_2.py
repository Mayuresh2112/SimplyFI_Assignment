# Function to calculate the minimum number of players to be shot
def min_players_to_be_shot(N, K, heights):
    count = 0
    for i in range(N):
        if heights[i] > K:
            count += 1
    return count

# Input reading and processing
T = int(input("Enter number of test cases: "))
for _ in range(T):
    N, K = map(int, input().split())
    heights = list(map(int, input().split()))

    # Calculate and print the result for each test case
    result = min_players_to_be_shot(N, K, heights)
    print(result)
