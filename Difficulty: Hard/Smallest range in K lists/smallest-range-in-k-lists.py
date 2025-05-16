class Solution:
    def findSmallestRange(self, arr):
        import heapq
        # code here
        k = len(arr)
        n = len(arr[0])
        
        min_heap = []
        curr_max = float('-inf')
        
        # Initialize heap with the first element of each list
        for i in range(k):
            heapq.heappush(min_heap, (arr[i][0], i, 0))
            curr_max = max(curr_max, arr[i][0])
        
        range_start, range_end = -1e5, 1e5  # Initialize with large range
    
        while True:
            curr_min, row, col = heapq.heappop(min_heap)
            
            # Update best range
            if curr_max - curr_min < range_end - range_start:
                range_start, range_end = curr_min, curr_max
    
            # Move to next element in the same row
            if col + 1 < n:
                next_val = arr[row][col + 1]
                heapq.heappush(min_heap, (next_val, row, col + 1))
                curr_max = max(curr_max, next_val)
            else:
                break  # One list exhausted, can't include all lists
    
        return [range_start, range_end]
        


#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())
for _ in range(t):
    n = int(input())
    k = int(input())
    arr = []
    for _ in range(k):
        arr.append(list(map(int, input().strip().split())))
    r = Solution().findSmallestRange(arr)
    print(r[0], r[1])
    print("~")

# } Driver Code Ends