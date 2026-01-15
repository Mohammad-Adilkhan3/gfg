class Solution:
    def minCandy(self, arr):
        # Code here
        N=len(arr)
        if N == 0:
            return 0
        left = [1] * N
        right = [1] * N
        for i in range(1, N):
            if arr[i] > arr[i - 1]:
                left[i] = left[i - 1] + 1
        for i in range(N - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                right[i] = right[i + 1] + 1
        candies = [max(left[i], right[i]) for i in range(N)]
        return sum(candies)