def pairWithMaxSum(self, arr):
        #code here
        if len(arr)<2:
            return -1
        M=-1
        n=len(arr)
        for i in range(n-1):
            m1=min(arr[i],arr[i+1])
            m2=max(arr[i],arr[i+1])
            curr=m1+m2
            M=max(M,curr)
        return M
        
