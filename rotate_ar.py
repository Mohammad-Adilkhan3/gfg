def rotateArr(self,A,D,N):
        #Your code here
        D = D % N 
        A[:] = A[D:] + A[:D]
  n,d=map(int,input().split())
a=list(map(int,input().split()))
print(rotateArr(a,d,n))
