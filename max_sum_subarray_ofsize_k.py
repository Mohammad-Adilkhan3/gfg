def maximumSumSubarray (self,K,Arr,N):
        # code here 
        cs = sum(Arr[:K])
        m = cs
        for i in range(K, N):
            cs = cs - Arr[i - K] + Arr[i]
            m = max(m, cs)
        return m
n,k=map(int,input().split())
a=list(map(int,input().split()))
print(maximumSumSubarray(k,a,n))
