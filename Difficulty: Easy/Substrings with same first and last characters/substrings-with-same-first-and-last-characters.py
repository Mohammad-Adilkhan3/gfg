class Solution:
	def countSubstring(self, s):
		# code here
		from collections import Counter
		freq = Counter(s)
        count = 0
        for f in freq.values():
            count += (f * (f + 1)) // 2
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.countSubstring(s)

        print(answer)
        print("~")

# } Driver Code Ends