#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
class Solution:
    def calculateSpan(self, arr):
        #write code here
        n = len(arr)
        stack = []  
        res = [0] * n  
        for i in range(n):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            if not stack:
                res[i] = i + 1
            else:
                res[i] = i - stack[-1]
            stack.append(i)
        
        return res
        

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.calculateSpan(arr)
        print(*ans)
        print("~")
        t -= 1
# } Driver Code Ends