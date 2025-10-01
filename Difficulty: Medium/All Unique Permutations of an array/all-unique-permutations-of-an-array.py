#User function Template for python3

class Solution:
    def uniquePerms(self, arr):
        # code here 
        n=len(arr)
        result = []
        visited = [False] * n
        current_permutation = []
    
        def backtrack():
            if len(current_permutation) == n:
                result.append(current_permutation.copy())
                return
    
            for i in range(n):
                if visited[i] or (i > 0 and arr[i] == arr[i - 1] and not visited[i - 1]):
                    continue
                visited[i] = True
                current_permutation.append(arr[i])
                backtrack()
                visited[i] = False
                current_permutation.pop()
    
        arr.sort()
        backtrack()
        return result


