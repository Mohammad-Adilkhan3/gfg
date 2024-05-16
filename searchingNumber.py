def search(self, n : int, k : int, arr : List[int]) -> int:
        # code here
        for i in arr:
            if k in arr:
                return arr.index(k)+1
        else:
            return -1
        
