class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        arr.sort()
        n=len(arr)
        i,j=0,n-1
        while i<j:
            arr.insert(i,arr.pop(j))
            i+=2
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.alternateSort(arr)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends