def countNumberswith4(self, n : int) -> int:
        # code here
        cnt=0
        for i in range(n+1):
            if "4" in str(i):
                cnt+=1
        return cnt
        
