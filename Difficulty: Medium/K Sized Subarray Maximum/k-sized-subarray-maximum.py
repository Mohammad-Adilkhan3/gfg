class Solution:
    def maxOfSubarrays(self, arr, k):
        # code here
        from collections import deque
        if not arr or k == 0:
            return []
        n = len(arr)
        result = []
        dq = deque()  # Stores indices of array elements
        for i in range(n):
            # Remove elements that are out of this window
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            # Remove elements smaller than the current element
            while dq and arr[dq[-1]] < arr[i]:
                dq.pop()
            # Add the current element index
            dq.append(i)
            # Append the maximum element for the current window
            if i >= k - 1:
                result.append(arr[dq[0]])
    
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        res = ob.maxOfSubarrays(arr, k)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
        print("~")
# } Driver Code Ends