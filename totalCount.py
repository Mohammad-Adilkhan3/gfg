def totalCount(self, k, arr):
        # code here
        cnt=0
        for i in arr:
            if i%k<k:
                cnt+=i//k
                if i%k!=0:
                    cnt+=1
        return cnt
