def rearrange(self,arr, n):
        # code here
        po=[i for i in arr if i>=0]
        neg=[i for i in arr if i<0]
        
        arr[:]=po[:]
        
        index=1
        for i in neg:
            arr.insert(index,i)
            index+=2
