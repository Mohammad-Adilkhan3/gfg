class Solution:
    def maxWater(self, arr):
        # code here
        l,r,res,a=0,len(arr)-1,0,0
        while l<r:
            if arr[l]< arr[r]:
                a=arr[l]* (r-l)
                l+=1
            else:
                a=arr[r]* (r-l)
                r-=1
            res=max(res,a)
        return res
            