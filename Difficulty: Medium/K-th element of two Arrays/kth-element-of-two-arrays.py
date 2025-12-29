#User function Template for python3


class Solution:

    def kthElement(self, a, b, k):
        res=sorted(a+b)
        return res[k-1]



