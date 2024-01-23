def leaders(self, A, N):
        #Code here
        result = []
        max_right = A[N - 1]
        result.append(max_right)
    
        for i in range(N - 2, -1, -1):
            if A[i] >= max_right:
                max_right = A[i]
                result = [max_right] + result
    
        return result
