class Solution:
    def findTwoElement(self, arr):
        # code here
        from collections import Counter
        C=Counter(arr)
        dup=miss=-1
        for i in C:
            if C[i]==2:
                dup=i
                break
        n=len(arr)
        tot=(n*(n+1))//2
        miss=abs(tot - (sum(arr)-dup))
        return [dup,miss]
