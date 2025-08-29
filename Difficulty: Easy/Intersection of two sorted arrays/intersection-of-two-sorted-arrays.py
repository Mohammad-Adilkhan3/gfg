class Solution:
    def intersection(self, arr1, arr2):
        #code here
        x=set(arr1) & set(arr2)
        y=sorted(list(x))
        return(y)
    
