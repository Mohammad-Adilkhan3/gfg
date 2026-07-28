class Solution:
    def shortestPath(self, V: int, src: int, dest: int, edges: list[list[int]]) -> int:
        # code here
        from collections import defaultdict
        import heapq
        adj=defaultdict(set)
        for sta,sto,dis in edges:
            adj[sta].add((sto,dis,))
            adj[sto].add((sta,dis))
        tot=[float('inf')]*V
        hp=[(0,src,)]
        while hp:
            dis,cur=heapq.heappop(hp)
            if tot[cur]<=dis:
                continue
            if cur==dest:
                return dis
            tot[cur]=dis
            for nxt,add in adj[cur]:
                heapq.heappush(hp,(dis+add,nxt,))
        return -1