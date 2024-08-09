def Maximize(self, arr):
        
        # Complete the function
        mod=1000000000+7
        s=0
        arr.sort()
        for i in range(len(arr)):
            s+=arr[i]*i
        return s%mod
