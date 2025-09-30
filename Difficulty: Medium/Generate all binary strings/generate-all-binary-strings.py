class Solution:
    def binstr(self, n):
        # code here
        res=[]
        for i in range(2**n):
            temp=['0']*n
            for j in range(n):
                if(i>>j)&1:
                    temp[n-j-1]='1'
            res.append(''.join(temp))
        return res
            
        