def isRepresentingBST(self, arr, N):
        # code here
        for i in range(1, N):
            if arr[i] <= arr[i - 1]:
                return 0  
        return 1 
n=int(input())
a=list(map(int,input().split()))
print(isRepresentingBST( a, n)
