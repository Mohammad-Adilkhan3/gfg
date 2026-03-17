class Solution:
    def findSubarray(self, arr):
        #code here.
        n=len(arr)
        s={}
        s[0]=1
        sum1=0
        c=0
        for i in range(n):
            sum1+=arr[i]
            if sum1 in s:
                c=c+s[sum1]
            if sum1 in s:
                s[sum1]=s[sum1]+1
            else:
                s[sum1]=1
        return c
