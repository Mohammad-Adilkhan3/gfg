class Solution:
    def rearrange(self, arr, x):
        # code here
        arr.sort(key=lambda i:abs(x-i))
        return arr
        