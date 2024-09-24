def firstNonRepeating(self, arr): 
        # Complete the function
        d={}
        for i in arr:
           if i not in d:
               d[i]=1
           else:
               d[i]+=1
        for i in arr:
           if d[i]==1:
               return i
        return 0    
