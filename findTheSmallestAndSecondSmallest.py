def minAnd2ndMin(self, arr):
        #code here
        if len(set(arr))==1:
            return [-1]
        else:
            return sorted(set(arr))[0:2]
