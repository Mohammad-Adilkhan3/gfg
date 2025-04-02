#User function Template for python3
from collections import deque
class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        # code here
        V = len(adj)  # Number of vertices
        visited = [False] * V  # Track visited nodes
        bfs_result = []  # Stores BFS order
        queue = deque([0])  # BFS queue starts with node 0
        visited[0] = True  # Mark starting node as visited
    
        while queue:
            node = queue.popleft()  # Dequeue front element
            bfs_result.append(node)  # Add to traversal result
            
            # Enqueue all unvisited neighbors in order
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
    
        return bfs_result


#{ 
 # Driver Code Starts
import sys


#Position this line where user code will be pasted.
def main():
    tc = int(sys.stdin.readline().strip())

    for _ in range(tc):
        V = int(sys.stdin.readline().strip())  # Number of vertices
        adj = []  # Adjacency list

        for _ in range(V):
            input_line = sys.stdin.readline().strip()
            node = list(map(int, input_line.split())) if input_line else []
            adj.append(node)

        obj = Solution()
        ans = obj.bfs(adj)
        print(" ".join(map(str, ans)))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends