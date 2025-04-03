#User function Template for python3

class Solution:
    def factorialNumbers(self, n):
    	#code here 
    	fact = 1
        i = 1
        factList = []
        while fact <= n:
            factList.append(fact)
            i += 1
            fact *= i
        return factList


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorialNumbers(N)
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends