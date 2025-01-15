# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        prefix_map = {}
        current_sum = 0
        max_length = 0
        
        for i, num in enumerate(arr):
            current_sum += num
            # Case 1: Subarray starting from the beginning
            if current_sum == k:
                max_length = max(max_length, i + 1)
            # Case 2: Subarray found ending at index i
            if (current_sum - k) in prefix_map:
                max_length = max(max_length, i - prefix_map[current_sum - k])
            # Case 3: Store the first occurrence of current_sum
            if current_sum not in prefix_map:
                prefix_map[current_sum] = i
        return max_length
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends