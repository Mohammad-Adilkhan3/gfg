def maxGold(self, n, m, M):
        # code here
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            dp[i][m - 1] = M[i][m - 1]
        for j in range(m - 2, -1, -1):
            for i in range(n):
                dp[i][j]=M[i][j]+max(dp[i][j+1],dp[i-1][j+1] if i > 0 else 0, dp[i + 1][j + 1] if i < n - 1 else 0)
        max_gold = 0
        for i in range(n):
            max_gold = max(max_gold, dp[i][0])
        return max_gold
n,m=map(int,input().split())
M=list(map(int,input().split()))
print(maxGold(n,m,M))
