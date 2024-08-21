def print2largest(self, arr):
        # Code Here
        s=set(arr)
        l=list(s)
        l.sort()
        
        if len(l)>=2:
            return l[-2]
        else:
            return -1
