class Solution:
    def combinationSum(self, n, k):
        # code here
        res=[]
        def backtrack(start,comb,curr_sum):
            if curr_sum==n and len(comb)==k:
                res.append(comb[:])
                return
            if curr_sum>n or len(comb)>k:
                return
            for i in range(start,10):
                comb.append(i)
                backtrack(i+1,comb,curr_sum+i)
                comb.pop()
        backtrack(1,[],0)
        return res
