class Solution:
    def longestSubarray(self, arr, x):
        from collections import deque
        left, max_deque, min_deque = 0, deque(), deque()
        best_start, max_length = 0, 0
    
        for right in range(len(arr)):
            while max_deque and arr[max_deque[-1]] <= arr[right]: max_deque.pop()
            while min_deque and arr[min_deque[-1]] >= arr[right]: min_deque.pop()
    
            max_deque.append(right)
            min_deque.append(right)
    
            while arr[max_deque[0]] - arr[min_deque[0]] > x:
                left += 1
                if max_deque[0] < left: max_deque.popleft()
                if min_deque[0] < left: min_deque.popleft()
    
            if right - left + 1 > max_length:
                best_start, max_length = left, right - left + 1
    
        return arr[best_start: best_start + max_length]
                
        
        


