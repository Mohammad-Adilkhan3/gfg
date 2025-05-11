from typing import List


class Solution:
    def kthLargest(self, arr, k) -> int:
        # code here
        n = len(arr)
        min_heap = []
        
        for start in range(n):
            current_sum = 0
            for end in range(start, n):
                current_sum += arr[end]
                if len(min_heap) < k:
                    heapq.heappush(min_heap, current_sum)
                elif current_sum > min_heap[0]:
                    heapq.heappushpop(min_heap, current_sum)
        
        return min_heap[0]

        



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import heapq

# Position this line where user code will be pasted.

#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        res = ob.kthLargest(arr, k)
        print(res)
        print("~")
        t -= 1

# } Driver Code Ends