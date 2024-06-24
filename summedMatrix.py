def sumMatrix(self, n, q):
        # code here 
        if q < 2 or q > 2 * n:
            return 0
        start = max(1, q - n)
        end = min(n, q - 1)
        if start > end:
            return 0
        return end - start + 1
