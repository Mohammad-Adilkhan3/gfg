def allPairs(self, A, B, N, M, X):
        # Your code goes here 
        arr = []
        for a in A:
            b = X - a
            if b in B:
                arr.append([a, b])
        return sorted(arr)
