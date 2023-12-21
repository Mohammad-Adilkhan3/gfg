def minCandy(N, ratings):
    if N == 0:
        return 0

    # Initialize left and right arrays
    left = [1] * N
    right = [1] * N

    # Traverse from left to right
    for i in range(1, N):
        if ratings[i] > ratings[i - 1]:
            left[i] = left[i - 1] + 1

    # Traverse from right to left
    for i in range(N - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            right[i] = right[i + 1] + 1

    # Calculate the minimum number of candies needed for each child
    candies = [max(left[i], right[i]) for i in range(N)]

    # Return the total minimum number of candies needed
    return sum(candies)

# Example usage:
N1 = 3
ratings1 = [1, 0, 2]
print(minCandy(N1, ratings1))  # Output: 5

N2 = 3
ratings2 = [1, 2, 2]
print(minCandy(N2, ratings2))  # Output: 4
