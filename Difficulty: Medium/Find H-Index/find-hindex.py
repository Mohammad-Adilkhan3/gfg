#User function Template for python3
class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        #code here
        n = len(citations)
        count = [0] * (n + 1)
        # Count the citations
        for c in citations:
            if c >= n:
                count[n] += 1
            else:
                count[c] += 1
        # Find the H-index
        h = 0
        for i in range(n, -1, -1):
            h += count[i]
            if h >= i:
                return i
        return 0


