class Solution:
    def findDuplicates(self, arr):
        # code here
        from collections import Counter
        C=Counter(arr)
        return [ i for i in C if C[i]==2]
        