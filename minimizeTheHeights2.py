def getMinDiff(self, arr,k):
        # code here
        n=len(arr)
        arr.sort()
        res=max(arr)-min(arr)
        for i in range(1,n):
            if arr[i]>k:
                mx=max(arr[i-1]+k,arr[n-1]-k)
                mn=min(arr[0]+k,arr[i]-k)
                res=(min(res,mx-mn))
        return res
