#User function Template for python3

class Solution:
	def binaryToDecimal(self, b):
		# Code here
		return int(b,2)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        str = input()
        ob = Solution()
        ans = ob.binaryToDecimal(str)
        print(ans)
        print("~")

# } Driver Code Ends