def pairsum(self, arr : List[int]) -> int:
        # code here
        n=len(arr)
        if n==1:
            return arr[0]
        arr.sort()
        return arr[n-1]+arr[n-2]
