
class Solution:
    def countDistinct(self, arr, k):
        # Code here
        if k > len(arr):
            return []
        freq_map = {}
        result = []
        # Initialize the first window
        for i in range(k):
            freq_map[arr[i]] = freq_map.get(arr[i], 0) + 1
        result.append(len(freq_map))
        # Slide the window
        for i in range(k, len(arr)):
            # Remove the element going out of the window
            out_elem = arr[i - k]
            freq_map[out_elem] -= 1
            if freq_map[out_elem] == 0:
                del freq_map[out_elem]
            # Add the element coming into the window
            in_elem = arr[i]
            freq_map[in_elem] = freq_map.get(in_elem, 0) + 1
            # Record the count of distinct elements
            result.append(len(freq_map))
        return result
        


#{ 
 # Driver Code Starts
import sys
from collections import defaultdict
if __name__ == '__main__':
    input = sys.stdin.read
    data = input().splitlines()
    t = int(data[0])
    index = 1
    while t > 0:
        arr = list(map(int, data[index].strip().split()))
        index += 1
        k = int(data[index])
        index += 1

        ob = Solution()
        res = ob.countDistinct(arr, k)

        for element in res:
            print(element, end=" ")
        print()
        print("~")

        t -= 1

# } Driver Code Ends