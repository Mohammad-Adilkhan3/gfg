class Solution:
    def maxLen(self, arr):
        # code here
        current_sum = 0
        max_length = 0
        sum_index_map = {0: -1}  # Initialize with 0 to handle edge cases
        
        for i, num in enumerate(arr):
            # Update current_sum
            current_sum += -1 if num == 0 else 1
            
            if current_sum in sum_index_map:
                # Subarray found
                max_length = max(max_length, i - sum_index_map[current_sum])
            else:
                # Store the first occurrence of current_sum
                sum_index_map[current_sum] = i
        
        return max_length


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    a = list(map(int, input().split()))
    s = Solution().maxLen(a)
    print(s)

# } Driver Code Ends