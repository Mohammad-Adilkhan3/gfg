#User function Template for python3

class Solution:
    def printNos(self, n):
        # Code here
        if n<1:
            return 1
        print(n,end=" ")
        return self.printNos(n-1)