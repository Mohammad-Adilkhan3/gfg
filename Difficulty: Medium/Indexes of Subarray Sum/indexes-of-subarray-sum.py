#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code here
        start = 0
        current_sum = 0
        for end in range(len(arr)):
            # Add the current element to the current_sum
            current_sum += arr[end]
            # Shrink the window from the left as long as current_sum > target
            while current_sum > target and start <= end:
                current_sum -= arr[start]
                start += 1
            # Check if we found the target
            if current_sum == target:
                return [start + 1, end + 1]  # Return 1-based indices
        # If no subarray is found
        return [-1]

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input().strip())
        ob = Solution()
        result = ob.subarraySum(arr, d)
        print(" ".join(map(str, result)))
        tc -= 1
        print("~")

# } Driver Code Ends