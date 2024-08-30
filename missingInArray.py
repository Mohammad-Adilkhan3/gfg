def missingNumber(self, n, arr):
        
        # code here
        return sum(range(1,n+1))-sum(arr)
