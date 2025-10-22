#User function Template for python3

class Solution:
    def nearlySorted(self, arr, k):
        #code
        import heapq
        heap = arr[:k + 1]
        heapq.heapify(heap)
        target_idx = 0
        for i in range(k + 1, len(arr)):
            arr[target_idx] = heapq.heappop(heap)
            target_idx += 1
            heapq.heappush(heap, arr[i])
        while heap:
            arr[target_idx] = heapq.heappop(heap)
            target_idx += 1


