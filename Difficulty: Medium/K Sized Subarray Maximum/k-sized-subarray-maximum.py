class Solution:
    def maxOfSubarrays(self, arr, k):
        import heapq
        #code here
        if not arr or k == 0:
            return []
        n = len(arr)
        result = []
        max_heap = []
        for i in range(n):
            heapq.heappush(max_heap, (-arr[i], i))
            while max_heap[0][1] <= i - k:
                heapq.heappop(max_heap)
            if i >= k - 1:
                result.append(-max_heap[0][0])  
    
        return result