#User function Template for python3
class Solution:
    def sumClosest(self, arr, target):
        # code here
        if len(arr) < 2:
            return []
        # Sort the array
        arr.sort()
        # Initialize two pointers
        low, high = 0, len(arr) - 1
        closest_diff = float('inf')
        best_pair = []
        while low < high:
            current_sum = arr[low] + arr[high]
            current_diff = abs(current_sum - target)
            # Update the best pair if a closer sum is found
            if current_diff < closest_diff or (
                current_diff == closest_diff and abs(arr[high] - arr[low]) > abs(best_pair[1] - best_pair[0])
            ):
                closest_diff = current_diff
                best_pair = [arr[low], arr[high]]
            # Move pointers based on comparison with the target
            if current_sum < target:
                low += 1
            else:
                high -= 1
        return best_pair




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    while t > 0:
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        ob = Solution()
        ans = ob.sumClosest(arr, target)
        if not ans:
            print("[]")
        else:
            print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends