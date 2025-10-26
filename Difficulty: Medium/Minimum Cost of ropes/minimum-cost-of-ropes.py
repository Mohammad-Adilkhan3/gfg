#User function Template for python3

class Solution:
    
    #Function to return the minimum cost of connecting the ropes.
    from typing import List
    def minCost(self, arr: List[int]) -> int:
        # code here
        import heapq
        
        heapq.heapify(arr)
        tc=0
        while len(arr)>1:
            f=heapq.heappop(arr)
            s=heapq.heappop(arr)
            c=f+s
            tc+=c
            heapq.heappush(arr,c)
        return tc
            
        


