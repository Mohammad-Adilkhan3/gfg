# Function should return an integer value
class Solution:
    def convertFive(self, n):
        # Code here
        s=str(n)
        S=s.replace('0','5')
        return S