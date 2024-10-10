def maxDistance(self, arr):
        # Code here
        occ={}
        res=0
        n=len(arr)
        for i in range(n):
            if arr[i] in occ:
                res=max(res,i-occ[arr[i]])
            else:
                occ[arr[i]]=i
        return res
