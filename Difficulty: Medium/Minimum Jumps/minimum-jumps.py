#User function Template for python3
class Solution:
    def minJumps(self, arr):
        #code here
        n=len(arr)
        if n==1:
            return 0
        if arr[0]==0:
            return -1
        jumps=1
        M=arr[0]
        step=arr[0]
        for i in range(1,n):
            if i==n-1:
                return jumps
            M=max(M,i+arr[i])
            step-=1
            if step==0:
                jumps+=1
                if i >= M:
                    return -1
                step+=M-i
        return -1





