def dfs(self, v, visited, adj, result):
        visited[v] = True
        result.append(v)
        
        for u in adj[v]:
            if not visited[u]:
                self.dfs(u, visited, adj, result)
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        visited = [False] * V
        result = []
        
        self.dfs(0, visited, adj, result)
        
        return result
