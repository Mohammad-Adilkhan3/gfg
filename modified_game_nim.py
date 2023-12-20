def findWinner(self, n, A):
        # code here
        if n%2==0:
            return 1
        v=0
        for i in A:
            v=v^i
        if v==0:
            return 1
        return 2
n=int(input())
a=list(map(int,input().split()))
res=findWinner(n,a)
print(res)
