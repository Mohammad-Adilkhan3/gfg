class Solution:
    def countValid(self, n, arr):
        # code here
        arr = set(arr)
        k = len(arr)
        total = 9 * 10**(n - 1)
        without = (9 - k + (0 in arr)) * (10 - k)**(n - 1)
        return total - without