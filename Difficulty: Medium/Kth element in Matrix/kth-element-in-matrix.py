class Solution:
    def kthSmallest(self, matrix, k):
        # code here
        import heapq
        n = len(matrix)
        min_heap = []
        for i in range(n):
            heapq.heappush(min_heap, (matrix[i][0], i, 0))
        count = 0
        while min_heap:
            val, r, c = heapq.heappop(min_heap)
            count += 1
            if count == k:
                return val
            if c + 1 < n:
                heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))
            