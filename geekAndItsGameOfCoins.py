def findWinner(n, x, y):
    # dp[i] will be True if the player whose turn it is to play can guarantee a win
    dp = [False] * (n + 1)

    # Base case: if there are 0 coins, the player to move loses
    dp[0] = False

    # Fill the dp array
    for i in range(1, n + 1):
        # Check if we can force the opponent into a losing state by picking 1, x, or y coins
        if i >= 1 and not dp[i - 1]:
            dp[i] = True
        elif i >= x and not dp[i - x]:
            dp[i] = True
        elif i >= y and not dp[i - y]:
            dp[i] = True

    return 1 if dp[n] else 0
