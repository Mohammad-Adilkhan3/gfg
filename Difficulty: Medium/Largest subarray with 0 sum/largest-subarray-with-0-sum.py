#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        sums = {}
        max_size = 0
        target = 0
        s = 0
        for i in range(n):
            s += arr[i]
            if target == s:
                max_size = i+1
            elif s - target in sums:
                max_size = max(max_size, i-sums[s-target])
            else:
                sums[s] = i
        return max_size


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends