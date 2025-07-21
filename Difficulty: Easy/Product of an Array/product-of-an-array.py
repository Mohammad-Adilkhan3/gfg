class Solution:
    # arr is the array
    def product(self, arr):
        # your code here
        result = 1
        mod = 1000000007
        for num in arr:
            result *= num
            result %= mod
        return result