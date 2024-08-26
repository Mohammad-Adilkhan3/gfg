def rearrange(self,arr, n): 
        ##Your code here
        res=[]
        lst=1
        fst=0
        
        for i in range((n//2)):
            res.append(arr[-lst])
            lst+=1
            res.append(arr[fst])
            fst+=1
            
        if n%2!=0:
            res.append(arr[-lst])
        
        arr[:]=res
