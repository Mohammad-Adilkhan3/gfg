def canSplit(self, arr):
        #code here
        ts=sum(arr)
        if ts%2!=0:
            return False
        req_sum=ts//2
        curr=0
        for i in arr:
            curr+=i
            if curr==req_sum:
                return True
        return False
