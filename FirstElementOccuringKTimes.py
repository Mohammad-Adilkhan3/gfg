def firstElementKTime(self,  a, n, k):
        # code here
        d = {}
        for i in a:
            if i not in d:
                d[i] = 1
            else:
                d[i] +=1
            if d[i] == k:
                return i 
        return -1
