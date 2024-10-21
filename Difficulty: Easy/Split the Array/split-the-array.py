#User function Template for python3
class Solution:
	def countgroup(self,arr): 
		#Complete the function
		m=10**9+7
		t=0
		for i in arr:
		    t^=i
		if t!=0:
            return 0
        return (pow(2, len(arr)-1, m) - 1) % m



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.countgroup(arr)
        print(res)
        t -= 1

# } Driver Code Ends