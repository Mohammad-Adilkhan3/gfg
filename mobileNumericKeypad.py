def number_of_sequences(n):
    # Mapping of each digit to its possible moves
    moves = {
        '0': ['0', '8'],
        '1': ['1', '2', '4'],
        '2': ['2', '1', '3', '5'],
        '3': ['3', '2', '6'],
        '4': ['4', '1', '5', '7'],
        '5': ['5', '2', '4', '6', '8'],
        '6': ['6', '3', '5', '9'],
        '7': ['7', '4', '8'],
        '8': ['8', '5', '7', '9', '0'],
        '9': ['9', '6', '8']
    }
    
    # Base case for n = 1, each digit is a sequence of length 1
    if n == 1:
        return 10
    
    # Initialize dp array where dp[i][j] means number of sequences of length i ending with digit j
    dp = [[0] * 10 for _ in range(n + 1)]
    
    # For sequences of length 1, there's one way to have each digit
    for j in range(10):
        dp[1][j] = 1
    
    # Fill the dp array for lengths 2 to n
    for i in range(2, n + 1):
        for j in range(10):
            for move in moves[str(j)]:
                dp[i][j] += dp[i - 1][int(move)]
    
    # Sum up all the sequences of length n starting from any digit
    result = sum(dp[n][j] for j in range(10))
    
    return result

# Example usage:
n = 5
print(number_of_sequences(n))  # Output: the number of possible sequences of length 5
