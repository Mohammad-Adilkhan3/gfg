"""
You're given an array (arr)
Return the frequency of element x in the given array
"""
class Solution:
    def findFrequency(self, arr, x):
        # code here
        from collections import Counter
        c=Counter(arr)
        for i in c:
            if i==x:
                return c[i]
        return 0