import math

def min_num_of_squares(n):
    # Initialize the dp array where dp[i] represents the minimum number of perfect squares summing to i
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # Base case

    # For each number up to n, find the minimum number of perfect squares required
    for i in range(1, n + 1):
        j = 1

        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1

    return dp[n]

# Smallest non-trivial logical input for debugging
n = 5
print(min_num_of_squares(n))
