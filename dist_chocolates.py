def findMinDiff(self, A,N,M):

        # code here
        A.sort()
        return min(A[_+M-1]-A[_] for _ in range(N-M+1))
n,m=map(int,input().split())
a=list(map(int,input().split()))
print(findMinDiff(a,n,m))
