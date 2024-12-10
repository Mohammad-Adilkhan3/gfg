#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def minRemoval(self, intervals):
        # Code here
        intervals.sort(key=lambda x: x[1])
        # Step 2: Initialize variables
        n = len(intervals)
        non_overlapping_count = 0
        prev_end = float('-inf')
        # Step 3: Iterate through intervals
        for start, end in intervals:
            if start >= prev_end:
                # Include this interval
                non_overlapping_count += 1
                prev_end = end
        # Step 4: Calculate and return the number of removed intervals
        return n - non_overlapping_count

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        intervals = [list(map(int, input().split())) for i in range(N)]
        ob = Solution()
        res = ob.minRemoval(intervals)
        print(res)
        print("~")
# } Driver Code Ends