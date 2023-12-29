def remove_duplicate(self, A, N):
		# code here
		if len(A) == 0:
            return 0
        j=0
        for i in range(1,len(A)):
            if A[i] != A[j]:
                j+=1
                A[j] = A[i]
        return j+1  
a=list(map(int,input().split()))
n=int(input())
res=remove_duplicate(a,n)
print(res)
