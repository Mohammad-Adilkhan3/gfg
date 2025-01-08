#User function Template for python3

class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # code here
        n=len(arr)
        arr.sort()
        cnt=0
        for k in range(2,n):
            i,j=0,k-1
            while i<j:
                if arr[i]+arr[j]>arr[k]:
                  cnt+=j-i
                  j-=1
                else:
                    i+=1
        return cnt

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.countTriangles(arr))

        print("~")

# } Driver Code Ends