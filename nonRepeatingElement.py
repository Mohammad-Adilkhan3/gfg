def firstNonRepeating(self, arr): 
        # Complete the function
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        # print(d)
        for i in d:
            if d[i]==1:
                return i
        return 0
