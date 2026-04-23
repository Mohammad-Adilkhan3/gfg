class Solution:
    def canSplit(self, arr):
        #code here
        if len(arr)<=1:
            return False
        s=sum(arr)
        ps=0
        i=len(arr)-1
        while i>=0:
            ps+=arr[i]
            s-=arr[i]
            if ps==s:
                return True
            i-=1
        return False