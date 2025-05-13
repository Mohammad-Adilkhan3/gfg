#User function Template for python3

class Solution:
    def nCr(self, n, r):
        # code here
        import math
        if(n<r):
            return 0
        if(n==r):
            return 1
        k=n-r
        n1=(math.factorial(n))
        r1=(math.factorial(r))
        nr=(math.factorial(k))
        k=(n1//(nr*r1))%(1000000007)
        return k
           







#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        r = int(input())
        ob = Solution()
        print(ob.nCr(n, r))
        print("~")
# } Driver Code Ends