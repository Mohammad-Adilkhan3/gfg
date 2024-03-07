def minCost(self,arr,n) :
    
        # code here
        heap = []

        for i in arr:
            heapq.heappush(heap, i)
        cost = 0
        while len(heap)>1:
            combine2SmallestRopes = heapq.heappop(heap)+heapq.heappop(heap)
            cost += combine2SmallestRopes
            heapq.heappush(heap, combine2SmallestRopes)
            
        return cost

