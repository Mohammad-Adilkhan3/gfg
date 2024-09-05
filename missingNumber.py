def missingNumber(self, n : int, arr : List[int]) -> int:
        # code here
        return sum(range(1,n+1))-sum(arr)
