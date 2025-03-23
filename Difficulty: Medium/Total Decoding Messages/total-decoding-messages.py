#User function Template for python3
class Solution:
	def countWays(self, digits):
		# Code here
		if digits[0]=='0' or not digits :return 0
		n = len(digits)
        prev2, prev1 = 1, 1  
    
        for i in range(1, n):
            current = 0
            if digits[i] != '0':  
                current += prev1  
            if 10 <= int(digits[i-1:i+1]) <= 26:  
                current += prev2  
    
            prev2, prev1 = prev1, current  
    
        return prev1  


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        digits = input()
        ob = Solution()
        ans = ob.countWays(digits)
        print(ans)
        print("~")

# } Driver Code Ends