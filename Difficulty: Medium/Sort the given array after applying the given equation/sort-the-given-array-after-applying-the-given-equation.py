class Solution:
	def sortArray(self, arr, A, B, C):
		# Code here
		res=[]
		for i in arr:
		    res.append(A*(i**2) + (B*i) +C)
		res.sort()
		return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        a = int(input())
        b = int(input())
        c = int(input())

        ob = Solution()
        ans = ob.sortArray(arr, a, b, c)
        print(' '.join(map(str, ans)))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends