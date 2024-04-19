def findMissing(self,a,b,n,m):
    # code here
        bs=set(b)
        res=[]
        for i in a:
            if i not in bs:
                res.append(i)
                
        return res
