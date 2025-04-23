#User function Template for python3

class Solution:
    from collections import Counter
	def singleNum(self, arr):
		# Code here
		res=[]
		x=self.Counter(arr)
		for i in x:
		    if x[i]==1:
		        res.append(i)
		return sorted(res)



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        ans = ob.singleNum(arr)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends