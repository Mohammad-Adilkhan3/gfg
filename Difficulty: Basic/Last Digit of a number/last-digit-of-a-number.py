#User function Template for python3
class Solution:
    def utility(self, n):
        # code here 
        ans = abs(n)%10;
        # Print ans
        print(ans)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        ob.utility(n)
        print('~')

# } Driver Code Ends