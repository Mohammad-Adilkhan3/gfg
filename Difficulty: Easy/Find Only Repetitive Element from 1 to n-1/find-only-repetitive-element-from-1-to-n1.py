#User function Template for python3
class Solution:
    def findDuplicate(self, arr):
        #code here
        n=len(arr)
        s=(n-1)*(n)//2
        return sum(arr)-s


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        print(ob.findDuplicate(arr))
        print("~")

# } Driver Code Ends