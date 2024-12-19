#User function Template for python3
class Solution:
    def kthMissing(self, arr, k):
        # code here
        left, right = 0, len(arr) - 1
    
        while left <= right:
            mid = (left + right) // 2
            missing = arr[mid] - (mid + 1)  # Count of missing numbers up to arr[mid]
            
            if missing < k:
                left = mid + 1
            else:
                right = mid - 1
        
        # After binary search, left is the position where missing >= k
        # Calculate the result:
        return left + k


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.kthMissing(A, D)
        print(ans)
        print("~")

# } Driver Code Ends